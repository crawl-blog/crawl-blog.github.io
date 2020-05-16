#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'granitosaurus'
SITENAME = '🕷 crawl.blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
DISPLAY_RSS_ON_MENU = True
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
COPYRIGHT_YEAR = 2019
FEED_DOMAIN = SITENAME
FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'

FOOTERITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)
SOCIAL = (
    ('github', 'https://github.com/crawl-blog'),
    ('mastodon', 'https://fosstodon.org/@crawlblog'),
    ('stack-exchange', 'https://stackoverflow.com/users/3737009/granitosaurus'),
    ('at', 'mailto:crawl.blog@pm.me'),
    ('matrix-org', 'https://matrix.to/#/#web-scraping:matrix.org'),
)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['img', 'video']
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['shortcodes']
THEME = 'dotrocks'
SHORTCODES = {
    'img': """<a href="/img/{{src}}"><img src="/img/{{src}}" title="{{desc}}"></img></a><figcaption>{{desc}}</figcaption>""",
    'mp4gif': """<video width="480" height="240" autoplay loop muted title="{{desc}}"><source src="/video/{{src}}" type="video/mp4"></video><figcaption>{{desc}}</figcaption>"""

}

# comments
UTTERANCES_REPO = 'crawl-blog/crawl-blog.github.io'
APPLAUSE_BUTTON = True
GOOGLE_ANALYTICS = "UA-132141387-1"
