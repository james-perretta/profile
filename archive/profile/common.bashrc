PATH=~/bin:$PATH

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

echo 'Loading common bash settings...'

# Settings adapted from the default linux mint 17 /etc/bash.bashrc file

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# source ~/profile/color.bashrc

# test -f ~/profile/bash_completion && source $_

PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\] \w \$\[\033[00m\] '


# ------------------------------------------------------------------------------

# My custom settings

#customize shell label
# export PS1="\u \w $ "

source ~/profile/git.git-completion.bash

BITBUCKET='git@bitbucket.org:james-perretta'

alias ls="ls $lsflags -Fh"
source ~/profile/my.aliases-bash
source ~/profile/my.functions-bash
