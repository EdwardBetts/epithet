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

def __build_url(**kwargs):
    return "%s?%s" % (POSTS_URL, urlencode(kwargs))
      
def getLinksByTags(*tags):
    tags = ','.join(tags)
    kw = dict(tag=tags, format='json')
    
    request_url = __build_url(**kw)
    header, body = __get_connection().request(request_url, 'GET')
    if header.status == 200:
        return json.loads(body)
