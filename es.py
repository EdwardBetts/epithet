#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
es.py - fetch pinboard.ed bookmarks, get concepts/keywords and index'em in elasticsearch
'''
__version__ = '0.1.0'
__license__ = "public domain"
__author__  = 'Luiz Rocha'

from httplib2 import Http
from utils import *
import alchemy
import pinboard
import json

http  = Http('.cache')
links = pinboard.getAllBookmarks()

for link in links:
    # print link
    pin_hash  = link['hash']
    pin_date  = link['time']
    pin_desc  = link['description']
    user_tags = link['tags'].split()
    url       = link['href']
    print url
    
    kw_res = alchemy.keywordExtract(url)['keywords']
    cn_res = alchemy.conceptExtract(url)['concepts']
    tags = cn_res+kw_res
    
    sort = lambda x: alchemy.sortByRelevance(x, 0.75)
    dash = lambda x: x.replace(' ', '-').lower()
    
    tags = map(sort, tags)
    tags = filter(lambda x: x, tags) # filtering None
    tags = map(dash, tags)
    # print tags
    
    tags = list(sorted(set(tags+user_tags)))
    print tags
    
    # to json
    body = json.dumps({'url': url, 'tags': tags, 'when': pin_date, 'desc': pin_desc})
    print body
    
    # send to elasticsearch
    pin_uri = 'http://localhost:9200/epithet/pin/%s' % pin_hash
    print pin_uri
    headers, body = http.request(pin_uri, 'PUT', body=body)
    print headers
    if headers.status in [200, 201, 204]:
        print "---------------- processed, continuing ----------------"
    else:
        break
