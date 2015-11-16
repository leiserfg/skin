# -*- coding: utf-8 -*-
"""
    skin._compat
    ~~~~~~~~~~~~

    Things to do it work on python 2 & 3

    :copyright: (c) 2014 by the Leiser Fernández Gallo.
    :license: BSD License.
"""
from __future__ import print_function
import sys


PY2 = sys.version_info[0] == 2


if PY2:
    string_types = basestring
    _input = raw_input
else:
    string_types = str
    _input = input


def input(msg=None):
    dec = lambda x: x.decode(sys.stdin.encoding)
    if msg:
        #raw_input can be tricki with unicode
        print(msg, end='')
    return dec(_input())


def to_unicode(txt, encoding='utf8'):
    if not isinstance(txt, string_types):
        txt = str(txt)
    if not PY2:
        return str(txt)
    if isinstance(txt, unicode):
        return txt
    return unicode(txt, encoding)
