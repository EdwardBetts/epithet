#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
epithet.py - a simple script to add context-based tags to pinboard.ed
'''
__version__ = '0.1.0'
__license__ = "public domain"
__author__ = 'Luiz Rocha'

from urllib import urlencode
from httplib2 import Http
import json

class Alchemy:
    KEYWORDS_URL = 'http://access.alchemyapi.com/calls/url/URLGetRankedKeywords'
    CONCEPTS_URL = 'http://access.alchemyapi.com/calls/url/URLGetRankedConcepts'
    
    def __init__(self, token):
        self._conn = Http('.cache')
        self._properties = dict(
            apikey = token,
            keywordExtractMode = 'strict',
            outputMode = 'json')

    def buildURL(self, api_root, **kw):
        return "%s?%s" % (api_root, urlencode(kw))

    def makeRequest(self, api_root, **kw):
        request_url = self.buildURL(api_root, **kw)
        header, body = self._conn.request(request_url, 'GET')
        if header.status == 200:
            return json.loads(body)

    def keywordExtract(self, url):
        kw = dict(url=url)
        kw.update(self._properties)
        extracted = self.makeRequest(self.KEYWORDS_URL, **kw)
        return extracted
        
    def conceptExtract(self, url):
        kw = dict(url=url)
        kw.update(self._properties)
        extracted = self.makeRequest(self.CONCEPTS_URL, **kw)
        return extracted
 
class Pinboard:
    POSTS_URL = 'https://api.pinboard.in/v1/posts/all'
    
    def __init__(self, user, pwd):
        self._conn = Http('.cache')
        self._conn.add_credentials(user, pwd)

    def buildURL(self, **kwargs):
        return "%s?%s" % (self.POSTS_URL, urlencode(kwargs))
    
    def getLinksByTags(self, *tags):
        tags = ','.join(tags)
        kw = dict(tag=tags, format='json')

        request_url = self.buildURL(**kw)
        header, body = self._conn.request(request_url, 'GET')
        if header.status == 200:
            return json.loads(body)

def lowercase(string):
    if isinstance(string, str) or isinstance(string, unicode):
        return string.lower()
    else:
        return None

def sortByRelevance(item, score):
    if float(item['relevance']) > score:
        return item['text']
    else:
        return None

if __name__ == '__main__':
    with open('pinboard.key', 'r') as f:
        pin_user, pin_pwd = f.readlines()
        pinboard = Pinboard(pin_user.strip(), pin_pwd.strip())
    
    with open('alchemy.key', 'r') as f:
        alchemy_key = f.readline()
        alchemy = Alchemy(alchemy_key.strip())
    
    links = pinboard.getLinksByTags('need_tags')
    
    for link in links:
        url = link['href']
        print(url)
        kw_res = alchemy.keywordExtract(url)['keywords']
        cn_res = alchemy.conceptExtract(url)['concepts']
        tags = cn_res+kw_res
        # print tags
        
        sort = lambda x: sortByRelevance(x, 0.75)
        tags = map(sort, tags)
        tags = map(lowercase, tags)
        tags = filter(lambda x: x, tags)
        tags = list(sorted(set(tags)))

        print tags

