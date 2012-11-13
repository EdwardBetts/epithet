# -*- coding: utf-8 -*-

__version__ = '0.1.0'
__license__ = "public domain"
__author__ = 'Luiz Rocha'


KEYWORDS_URL = 'http://access.alchemyapi.com/calls/url/URLGetRankedKeywords'
CONCEPTS_URL = 'http://access.alchemyapi.com/calls/url/URLGetRankedConcepts'


def sortByRelevance(item, score):
    if float(item['relevance']) > score:
        return item['text']
    else:
        return None