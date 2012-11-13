# -*- coding: utf-8 -*-

def lowercase(string):
    if isinstance(string, str) or isinstance(string, unicode):
        return string.lower()
    else:
        return None

