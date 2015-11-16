# -*- coding: utf-8 -*-
"""
    skin.cli
    ~~~~~~~~

    Console interface of skin

    :copyright: (c) 2014 by the Leiser Fernández Gallo.
    :license: BSD License.
"""
import os
from argparse import ArgumentParser
from completion import completion
from os import getcwd
from os.path import abspath

from core import list_skins, render_skin, TEMPLATES_DIR

parser = ArgumentParser(description="Project templates filler", prog='skin')
exclusives_group = parser.add_mutually_exclusive_group()
exclusives_group.add_argument(
    '-l', '--list', action='store_true', help='List all templates')
exclusives_group.add_argument(
    '-b', '--bash', action='store_true', help='Bash Completion')
exclusives_group.add_argument(
    '-z', '--zsh', action='store_true', help='Zsh Completion')
exclusives_group.add_argument(
    '-f', '--fish', action='store_true', help='Fish Completion')
parser.add_argument('template',
                    help='Render a template in the '
                         'current working directory',
                    nargs='?')
parser.epilog = "Put your own templates at: %s\n" % TEMPLATES_DIR[0]

# TODO: make it in a beautyfull way (maybe by using commands)
_args = ['-l', '--list', '-b', '--bash', '-z', '--zsh', '-f', '--fish']


def autocomplete():
    if 'SKIN_AUTO_COMPLETE' not in os.environ:
        return
    cwords = os.environ['COMP_WORDS'].split()[1:]
    cword = int(os.environ['COMP_CWORD'])
    try:
        current = cwords[cword - 1]
    except IndexError:
        current = ''
    if current.startswith('-'):
        print ' '.join(a for a in _args if a.startswith(current))
    print '\n'.join(t for t in list_skins() if t.startswith(current))
    exit(1)


def main():
    autocomplete()
    args = parser.parse_args()
    if args.list:
        for t in list_skins():
            print t
        return
    elif args.bash:
        completion('bash')
    elif args.zsh:
        completion('zsh')
    elif args.fish:
        completion('fish')
    elif args.template:
        render_skin(args.template, abspath(getcwd()))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
