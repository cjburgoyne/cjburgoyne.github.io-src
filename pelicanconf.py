#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chris Burgoyne'
SITENAME = u'Chris Burgoyne'
SITEURL = u'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = u'Analytics and Data Visualization'

PATH = 'content'
THEME = '../pelican-themes/Flex'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAINMENU = True

# Blogroll
LINKS = (('bl.ocks', 'https://bl.ocks.org/cjburgoyne'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/chrisjburgoyne'),
          ('github', 'https://github.com/cjburgoyne'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
