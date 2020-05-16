Title: parselcli - css and xpath selectors in your terminal!
Date: 2019-03-28
Tags: python, parsel, parsing
summary: I'd like to introduce `parselcli` an command line application for evaluating css and xpath selectors in your terminal.

Building html parser can be quite time consuming and often complicated. [parsel](https://github.com/scrapy/parsel) is a python library for parsing html with css or xpath selectors, while [parselcli](https://github.com/Granitosaurus/parsel-cli) is an interactive shell wrapper around it.

_Disclaimer: I wrote parselcli_

In short `parselcli` allows you to do this:

<script id="asciicast-234118" src="https://asciinema.org/a/234118.js" async></script>

At the moment version 0.31 `parselcli` has these features:

* css and xpath selectors
* Auto complete for classes, ids and tags with history (for ptpython shell)
* Evaluating against cached, live urls or local files (see --cached and --file flags)
* Inline executions:

        $ parsel "http://httpbin.org/html" -c h1
        ['<h1>Herman Melville - Moby-Dick</h1>']
  
* Supports output processors:

        $ parsel "http://httpbin.org/html" -c h1::text -p join,len
        27
        # the h1 text is 27 characters long!
    
* Supports commands for fast workflow and debuging:

        $ parsel "http://httpbin.org/html"
        > -help
        available commands (use -command):
          help: show help
          debug: show debug info
          embed: start interactive python shell
          open: open current url in browser tab
          view: open current html in browser tab
          fetch: download from new url
          css: switch to css selectors
          xpath: switch to xpath selectors
          
* Fully configurable via `~/.config/parsel.toml` file (depending on your `$XDG_CONFIG`)
* Preload embed shell for full python

        $ parsel "http://httpbin.org/html" --embed
        >>> dir()
        ['request', 'response', 'sel']
        >>> response.cookies
        <RequestsCookieJar[]>


## My Workflow 

I build `parselcli` to have faster and more convenient workflow for building html parsers.

[% mp4gif src=spongebob_work.mp4 %]

First thing I do is find a product/item that has the higher coverage. For example if I'm crawling a clothing shop I look for a product that has all of the fields like variants, colours, sizes and multiple prices. Shoes in often meet this criteria.   
This will be my _genesis_ html that I will use to build my parser.

I pass this url to my `parsel` and cache it in case I need to run it again in the future. 

    $ parsel "http://httpbin.org/html" --cache
    using cached version
    > 

Afterwards if the website functions without javascript I use `-view` command to open up source in my browser or `-open` command to open up live url in my browser.  

In my browsers (chromium or qutebrowser) I open up inspector and click around html code and identify my css selectors if they are possible, xpath if something more complicated is required.  
I pop my ideas to parsel shell and see how it looks.

    > h1::text
    ['Herman Melville - Moby-Dick']

If I'm satisfied I save the selectors in my crawler code and move on.  
Quite simple really!

## Contribution is Welcome!

Parselcli is still in rather early development but I've been using it _in production_ for a while now. Nevertheless any contributions are welcome!

[% img src=parselcli_releases.png %]

https://github.com/Granitosaurus/parsel-cli
