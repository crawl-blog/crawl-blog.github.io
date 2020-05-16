Title: Why Do We Crawl The Web?
Date: 2019-01-19
Tags: general, politics, design, industry
Slug: why-do-we-crawl
summary: Why do we crawl websites? What projects are being born from gathered public data and how can that help a business or society as a whole?

Whenever people ask me what I do for a living it's a bit hard to explain. People are no longer satisfied with "I'm a programmer" and often they follow up with a question: "What do you program?". "I write programs that retrieve data from websites" is usually enough for an answer but I feel that people don't really understand _why_ someone would want that.

A lot of new programmers often struggle with project ideas and the biggest bootstrap you can get is data. There are public data sets but they are often boring and dated - what really kickstarts a project is real time, fresh and juicy information!

The point of this particular entry is to cover these two cases: explain the industry and provide pointers for crawling projects.

# Trade Listings

One of the most common crawling subjects are just trade listings. Whether it's ebay, craiglist, car dealerships or job offers - it's valuable data and interesting data that can bootstrap so many ideas!

My most common beginner project idea for students is making a notification crawler - a crawler that would crawl something and email, twitter or push notification to a phone when some condition is met.

[% img src=listings.png %]

For example I'm looking for a used Honda Civic that is no older than 10 years and is color blue. Also turns out that relatively recent blue Honda Civics are in high demand, so I want to know about it ASAP. Here a web-crawler performs a perfect function. Check the website every 5 minutes for Blue Honda Civic listings and if there's something pop an email!

[% img src=data-board.svg desc="turns out honda civic might not be a good investment after all" %]

Even more common usage for listing crawlers is just to hoard data for marketing and data analysis. A lot of wise decisions can be made by looking at historic trends, be it your competition or just general market.


# E-commerce

It's almost identical case as trade listings - mostly crawled for marketing or tracking. This is probably the most common crawler type in the industry as there's huge demand for product data - observing competition is vital part of any marketing.

[% img src=ecommerce.svg desc="I can see what you're doing!" %]

Not only that but companies are also interested in how well their own products are doing. I've worked on projects that offer services for brands an overview of their products by crawling a bunch of their retailers for reviews, pricing and whether the retailers aren't breaking any agreements. These types of services have been rising in popularity lately.

# Leads

You've probably heard this term before and discarded it as one of those marketing words that everyone uses but nobody knows what it means. Well you're kinda right - leads can mean so many things, but it's a very popular subject for web crawling and it usually means _marketing target or object_.

This information is on high demand as it's extremely useful for marketing and general statistics. You'd like to know all companies located in US, Texas that work in video game industry? People that have github and gitlab accounts so you can do gitlab migration statistics?

[% img src=boss.svg desc="Oddly specific but I think we can crawl that" %]

The possibilities are _endless_ for marketing and various sciency activities. Crawlers in this medium also tend to be quite challenging because of the sheer scale of the projects.

# Humanitarian Causes

If there's data there's probably some way to use that data to improve our society!

[% img src=scientist.svg desc="if scientists had access to web-crawling" %]

Unfortunately this is still a developing medium in web crawling, but there's a lot of potential to bring real change through web-crawling. The biggest issue is that people just are afraid to create and share such datasets and crawlers because of the absurd copyright laws and aggressive behaviour by the data source companies. Fortunately cases against crawlers never win in the actual court but the fear of _going_ to court is often enough of a deterrent to stop any sort of public crawlers.

Various government and charity organizations need data and often the domains either refuse to provide it, charge ludicrous prices or the subject just covers hundreds of domains making it just easier and more efficient to crawl the data.

> One of the most interested cases I've been brought to was crawling of various escort forums in USA to gather escort data to detect human trafficking.

All that being said there's still a movement for __public datasets__ - crawled data that is shared publicly for various open projects.

[% img src=all_welcome.svg desc="open data set guys are like knowledge sharing buddhas <3" %]

* [commoncrawl.org] - The biggest open data set on website raw data, text and metadata extract.
* [sajari.com/public-data] - Curated list of public data sets from various sources.

# Real Time Data

The most common form of crawling in __applications__ is crawling of real time data. Common example would be a sports match crawler that would crawl match data. These types of crawlers are very popular in floss as the apps tend to be self sufficient (don't need central service). The biggest real time crawler would be `youtube-dl` which crawls many media pages and parses them for direct media sources.

This is also a great medium for beginners since it avoids the complex parts of crawling that is asynchronous logic and crawler scaling. A task I often recommend for beginners is usually sports notification crawler - crawling sports data and notifying about results via email or push notification.

[% img src=dood.svg desc="spiders can be like your personal assistants!" %]

# Meta Crawling

By far the most common industry crawling is meta crawling: google, microsoft, amazon - every big data company does some sort of meta crawling. Unfortunately it's by far the most boring niche and it rarely has any application outside from mega corporation indexing things and little widgets (like url previews you get in messaging applications).


# Data!

These are just few broad ideas of what are the uses of web-crawling but there are many more specific applications that I didn't cover, so if you're ever struggling with project idea skim around the web - there's so much amazing public data that you can use to play around or even start a business!

Unfortunately the outdated copyright laws and some abusive behaviour by some corporate entities tend to scare people away from this medium and give it a bad name but people shouldn't be deterred of entering this exciting medium!

> Spiders are lovely creatures and in general they are a net benefit to our society!

## Credits And Licensing

All of the images are made using vector files provided by [svgrepo.com] and modified in [Inkscape].

[commoncrawl.org]: http://commoncrawl.org/the-data/
[sajari.com/public-data]: https://www.sajari.com/public-data
[svgrepo.com]: http://scvrepo.com
[Inkscape]: http://inkscape.org
