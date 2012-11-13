#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
epithet.py - a simple script to add context-based tags to pinboard.ed
'''
__version__ = '0.1.0'
__license__ = "public domain"
__author__ = 'Luiz Rocha'

from utils import *
import alchemy
import pinboard

links = pinboard.getLinksByTags('need_tags')

for link in links:
    url = link['href']
    print(url)
    # kw_res = alchemy.keywordExtract(url)['keywords']
    # cn_res = alchemy.conceptExtract(url)['concepts']
    # tags = cn_res+kw_res
    # # print tags
    # 
    # sort = lambda x: sortByRelevance(x, 0.75)
    # tags = map(sort, tags)
    # tags = map(lowercase, tags)
    # tags = filter(lambda x: x, tags)
    # tags = list(sorted(set(tags)))
    # 
    # print tags
# 
# 
# 
# 
#  
# class Pinboard:
#     def __init__(self, user, pwd):
#         self._conn = Http('.cache')
#         self._conn.add_credentials(user, pwd)
# 
#     def buildURL(self, **kwargs):
#         return "%s?%s" % (self.POSTS_URL, urlencode(kwargs))
#     
#     def getLinksByTags(self, *tags):
#         tags = ','.join(tags)
#         kw = dict(tag=tags, format='json')
# 
#         request_url = self.buildURL(**kw)
#         header, body = self._conn.request(request_url, 'GET')
#         if header.status == 200:
#             return json.loads(body)
# 
# 
# 
# class Alchemy:
#     KEYWORDS_URL = 'http://access.alchemyapi.com/calls/url/URLGetRankedKeywords'
#     CONCEPTS_URL = 'http://access.alchemyapi.com/calls/url/URLGetRankedConcepts'
# 
#     def __init__(self, token):
#         self._conn = Http('.cache')
#         self._properties = dict(
#             apikey = token,
#             keywordExtractMode = 'strict',
#             outputMode = 'json')
# 
#     def buildURL(self, api_root, **kw):
#         return "%s?%s" % (api_root, urlencode(kw))
# 
#     def makeRequest(self, api_root, **kw):
#         request_url = self.buildURL(api_root, **kw)
#         header, body = self._conn.request(request_url, 'GET')
#         if header.status == 200:
#             return json.loads(body)
# 
#     def keywordExtract(self, url):
#         kw = dict(url=url)
#         kw.update(self._properties)
#         extracted = self.makeRequest(self.KEYWORDS_URL, **kw)
#         return extracted
# 
#     def conceptExtract(self, url):
#         kw = dict(url=url)
#         kw.update(self._properties)
#         extracted = self.makeRequest(self.CONCEPTS_URL, **kw)
#         return extracted