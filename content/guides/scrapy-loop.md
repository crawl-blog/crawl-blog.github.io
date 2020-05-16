Title: Scrapy: How to loop a crawler
Date: 2019-03-28
tags: scrapy,python
slug: scrapy-loop
summary: Explore ways to properly loop scrapy crawlers with twisted callbacks.

Running scrapy crawlers from a script is not difficult, however things start to get more complicated once additional logic needs to be injected. Like if you want to run crawler in an endless loop!

[% img src=ouroboros.gif %]

There are a lot of ways to do this but by since scrapy is using Twisted for crawl loop you can extend the same loop with your on callbacks and errorbacks.
This is how you run scrapy with a script:

    import scrapy
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings

    class MySpider(scrapy.Spider):
        # Your spider definition
        ...

    process = CrawlerProcess(get_project_settings())

    process.crawl(MySpider)
    process.start() # the script will block here until the crawling is finished

The interesting bit here is that `process.crawl(MySpider)` actually returns twisted's deferred! We can attach some callbacks to this deferred that will be fired once the crawl finished.
In other words if we want to have an endless loop we can just add a recursive callback - once crawl finishes, crawl again!

    process = CrawlerProcess(get_project_settings())

    def _crawl(result, spider):
        deferred = process.crawl(spider)
        deferred.addCallback(_crawl, spider)
        return deferred

    _crawl(None, Myspider)
    process.start()

Now once crawl finished another will start immediately!

### Improvements

We can still improve on this. First we can __add a sleep__ between calls for cases where we want to run crawler only so often.

    from twisted.internet import reactor
    from twisted.internet.task import deferLater


    def sleep(self, *args, seconds):
        """Non blocking sleep callback"""
        return deferLater(reactor, seconds, lambda: None)


    process = CrawlerProcess(get_project_settings())


    def _crawl(result, spider):
        deferred = process.crawl(spider)
        deferred.addCallback(lambda results: print('waiting 100 seconds before restart...'))
        deferred.addCallback(sleep, seconds=100)
        deferred.addCallback(_crawl, spider)
        return deferred


    _crawl(None, MySpider)
    process.start()

Finally we should __handle crashes__. For this we can use errorbacks which will be called if an unhandled exception happens:
    
    def crash(failure):
        print('oops, spider crashed')
        print(failure.getTraceback())
    
    def _crawl(result, spider):
        deferred = process.crawl(spider)
        deferred.addCallback(lambda results: print('waiting 100 seconds before restart...'))
        deferred.addErrback(crash)  # <-- add errback here
        deferred.addCallback(sleep, seconds=100)
        deferred.addCallback(_crawl, spider)
        return deferred

Here if crawler crashes we'll print a message and close the process.

### More Ideas

You can add as many `Errbacks` and `Callbacks` as you want and you can get quite creative with this approach. Send a slack message, check crawler stats, maybe even chain multiple different crawlers!

### Full Implementations

I wrote a small example with full capabilities like logging, configured intervals and hooks that I used in production with great success.  
Check out [scrapy-loop on gitlab](https://gitlab.com/granitosaurus/scrapy-loop)

-------
##### Attributions
The beautiful ouroboros gif is provided by [Akhil Dakinedi](http://akhildakinedi.com/)
