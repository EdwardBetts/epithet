# -*- coding: utf-8 -*-

__license__ = "public domain"
__author__  = 'Luiz Rocha'

from httplib2 import Http
from urllib import urlencode
import json

from settings import ALCHEMY_KEY

KEYWORDS_URL = 'http://access.alchemyapi.com/calls/url/URLGetRankedKeywords'
CONCEPTS_URL = 'http://access.alchemyapi.com/calls/url/URLGetRankedConcepts'

def __query_params(target_url):
    qs = dict(url=target_url,
            apikey = ALCHEMY_KEY,
            keywordExtractMode = 'strict',
            outputMode = 'json')
    return qs

def __make_request(base_url, **kw):
    request_url = "%s?%s" % (base_url, urlencode(kw))
    header, body = Http('.cache').request(request_url, 'GET')
    if header.status == 200:
        return json.loads(body)
    else:
        print header.status
        print body
        return None

def keywordExtract(target_url):
    kw = __query_params(target_url)
    extracted = __make_request(KEYWORDS_URL, **kw)
    return extracted

def conceptExtract(target_url):
    kw = __query_params(target_url)
    extracted = __make_request(CONCEPTS_URL, **kw)
    return extracted

def sortByRelevance(item, score):
    if float(item['relevance']) > score:
        return item['text']
    else:
        return None