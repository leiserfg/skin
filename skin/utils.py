#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import getpass
from os import remove, getcwd
from shutil import rmtree
from os.path import isfile, isdir, abspath
from subprocess import call

from helpers import pformat
try:
    input = raw_input
except NameError:
    pass



def prompt(text, default=None, _test=None):
    """Ask a question via raw_input() and return their answer.

    param text: prompt text
    param default: default value if no answer is provided.
    """

    text += ' [%s]' % default if default else ''
    while True:
        if _test is not None:
            print(text)
            resp = _test
        else:
            resp = input(text)
        if resp:
            return resp.decode('utf-8')
        if default is not None:
            return default


def prompt_bool(text, default=False, yes_choices=None, no_choices=None,
                _test=None):
    """Ask a yes/no question via raw_input() and return their answer.

    :param text: prompt text
    :param default: default value if no answer is provided.
    :param yes_choices: default 'y', 'yes', '1', 'on', 'true', 't'
    :param no_choices: default 'n', 'no', '0', 'off', 'false', 'f'
    """

    yes_choices = yes_choices or ('y', 'yes', 't', 'true', 'on', '1')
    no_choices = no_choices or ('n', 'no', 'f', 'false', 'off', '0')

    default = yes_choices[0] if default else no_choices[0]
    while True:
        if _test is not None:
            print(text)
            resp = _test
        else:
            resp = prompt(text, default)
        if not resp:
            return default
        resp = str(resp).lower()
        if resp in yes_choices:
            return True
        if resp in no_choices:
            return False


def echo_off_prompt(text, default=None, _test=None):
    """Ask a question via getpass() and return their answer.

    param text: prompt text
    param default: default value if no answer is provided.
    """

    text += ' [%s]' % default if default else ''
    while True:
        if _test is not None:
            print(text)
            resp = _test
        else:
            resp = getpass(text)
        if resp:
            return resp.decode('utf-8')
        if default is not None:
            return default
