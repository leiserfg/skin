# -*- coding: utf-8 -*-
"""
    skin.utils
    ~~~~~~~~~~

     Functions used internally and on the skins.

    :copyright: (c) 2011 by the Werkzeug Team, see AUTHORS for more details.
    :license: BSD License.
"""

from getpass import getpass

from _compat import input
from _santoral import rand_name

RULES_UTILS = ("prompt", "prompt_bool", "echo_off_prompt", "rand_name")


def prompt(text, default=None, _test=None):
    """Ask a question via raw_input() and return their answer.

    param text: prompt text
    param default: default value if no answer is providedself.
    """

    text += ' [%s]' % default if default else ''
    text += ': '
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
    text += ': '
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
