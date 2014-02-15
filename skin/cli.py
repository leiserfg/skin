# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser
import colorama
import kernel
import tools

parser = ArgumentParser(description="Project templates filler", prog='skin')
exclusives_group = parser.add_mutually_exclusive_group()
exclusives_group.add_argument(
    '-l', '--list', action='store_true', help='List all templates')
exclusives_group.add_argument(
    '-b', '--bash', action='store_true', help='Bash Completion')
exclusives_group.add_argument(
    '-z', '--zsh', action='store_true', help='Zsh Completion')
parser.add_argument('template',
                    help='Render a template in the'
                         'current working directory',
                    nargs='?')
parser.epilog = "Put your own templates at: %s\n" % kernel._templates_dirs[0]

# TODO: make it in a beautyfull way (maybe by using commands)
_args = ['-l', '--list', '-b', '--bash', '-z', '--zsh']


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
    print '\n'.join(t for t in kernel.templates() if t.startswith(current))
    exit(1)


def main():
    autocomplete()
    colorama.init()
    args = parser.parse_args()
    if args.list:
        for t in kernel.templates():
            print t
        return
    elif args.bash:
        tools.completion('bash')
    elif args.zsh:
        tools.completion('zsh')
    elif args.template:
        kernel.render(args.template)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
