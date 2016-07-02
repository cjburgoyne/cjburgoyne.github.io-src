#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chris Burgoyne'
SITENAME = u'Chris Burgoyne'
SITEURL = u'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = u'Analytics and Data Visualization'

ROBOTS = u'index, follow'

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

MAIN_MENU = True

# Blogroll
LINKS = (('bl.ocks', 'https://bl.ocks.org/cjburgoyne'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/chrisjburgoyne'),
          ('github', 'https://github.com/cjburgoyne'),
          ('linkedin', 'https://linkedin.com/pub/christopher-burgoyne/11/402/a07'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
