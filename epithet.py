#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
epithet.py - a simple script to add context-based tags to pinboard.ed
'''
__version__ = '0.2.0'
__license__ = "public domain"
__author__  = 'Luiz Rocha'

from utils import *
import alchemy
import pinboard

links = pinboard.getLinksByTags('need_tags')

for link in links:
    url = link['href']
    print(url)
    kw_res = alchemy.keywordExtract(url)['keywords']
    cn_res = alchemy.conceptExtract(url)['concepts']
    tags = cn_res+kw_res
    # print tags
    
    sort = lambda x: alchemy.sortByRelevance(x, 0.75)
    tags = map(sort, tags)
    tags = map(lowercase, tags)
    tags = filter(lambda x: x, tags)
    tags = list(sorted(set(tags)))
    
    print tags
