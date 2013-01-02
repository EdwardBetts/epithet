# -*- coding: utf-8 -*-

__license__ = "public domain"
__author__  = 'Luiz Rocha'

from httplib2 import Http
from urllib import urlencode
import json

from settings import PINBOARD_USER, PINBOARD_PWD

POSTS_URL = 'https://api.pinboard.in/v1/posts/all'

def __get_connection():
    _conn = Http('.cache')
    _conn.add_credentials(PINBOARD_USER, PINBOARD_PWD)
    return _conn

def __build_url(qs):
    return "%s?%s" % (POSTS_URL, urlencode(qs))

def __fetch_and_parse_bookmarks(qs):
    request_url = __build_url(qs)
    header, body = __get_connection().request(request_url, 'GET')
    if header.status == 200:
        return json.loads(body)

def getBookmarksByTags(*tags):
    tags = ','.join(tags)
    qs = { 'tag': tags, 'format': 'json' }
    return __fetch_and_parse_bookmarks(qs)

def getAllBookmarks():
    qs = { 'format': 'json' }
    return __fetch_and_parse_bookmarks(qs)
