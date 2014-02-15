# -*- coding: utf-8 -*-
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
"""}


def completion(shell):
    shell_options = COMPLETION_SCRIPTS.keys()
    if shell in shell_options:
        print COMPLETION_SCRIPTS[shell]
    else:
        sys.stderr.write('ERROR: You must pass %s\n' %
                         ' or '.join(shell_options))
