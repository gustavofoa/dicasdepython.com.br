#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://dicasdepython.com.br'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Plugins
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'minify', 'tag_cloud']

SITEMAP = {
    'format': 'xml',
    'exclude': ['autor/', 'tag/', 'categoria/', 'arquivo/'],
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Following items are often useful when publishing

DISQUS_SITENAME = "dicas-de-python"


MINIFY = {
 'remove_comments': True,
 'remove_all_empty_space': True,
 'remove_optional_attribute_quotes': False
}
