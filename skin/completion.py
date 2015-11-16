# -*- coding: utf-8 -*-
"""
    skin.completion
    ~~~~~~~~~~~~~~~

    Stuff for completion on diferents shells (currently bash and zsh)

    :copyright: (c) 2014 by the Leiser Fernández Gallo.
    :license: BSD License.
"""
from __future__ import print_function
import sys


COMPLETION_SCRIPTS = {
    'bash': """
_skin_completion()
{
    COMPREPLY=( $( COMP_WORDS="${COMP_WORDS[*]}" \\
                   COMP_CWORD=$COMP_CWORD \\
                   SKIN_AUTO_COMPLETE=1 $1 ) )
}
complete -o default -F _skin_completion skin
""",
    'zsh': """
function _skin_completion {
  local words cword
  read -Ac words
  read -cn cword
  reply=( $( COMP_WORDS="$words[*]" \\
             COMP_CWORD=$(( cword-1 )) \\
             SKIN_AUTO_COMPLETE=1 $words[1] ) )
}
compctl -K _skin_completion skin
""",
    'fish': """
    complete -c skin -x -a '(skin -l)'
    """
}


def completion(shell):
    try:
        print(COMPLETION_SCRIPTS[shell])
    except KeyError:
        sys.stderr.write('ERROR: You must pass %s\n' %
                         ' or '.join(COMPLETION_SCRIPTS))
