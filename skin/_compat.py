# -*- coding: utf-8 -*-
"""
    skin._compat
    ~~~~~~~~~~~~

    Things to do it work on python 2 & 3

    :copyright: (c) 2014 by the Leiser Fernández Gallo.
    :license: BSD License.
"""
import sys


PY2 = sys.version_info[0] == 2


if PY2:
    string_types = basestring
    _input = raw_input
else:
    string_types = str
    _input = input

def input(msg=None):
    if msg:
        msg = to_unicode(msg)
        return to_unicode(_input(msg))

    return to_unicode(_input())


def to_unicode(txt, encoding='utf8'):
    if not isinstance(txt, string_types):
        txt = str(txt)
    if not PY2:
        return str(txt)
    if isinstance(txt, unicode):
        return txt
    return unicode(txt, encoding)
