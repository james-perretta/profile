#customize shell label
# export PS1="\u \w $ "

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

echo 'Loading mac bash settings...'

go_bin='/usr/local/go/bin'
#dart_bin='~/bin/dart-sdk/bin'
eecs280_utils="$HOME/cs/eecs/280/scripts-and-utils"
export PATH="/Library/TeX/texbin:eecs280_utils:$go_bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/sbin"

lsflags="-G"

alias trash='trash -v'

alias snes='wine "C:\Program Files\zsnes\zsnesw.exe" &'

alias python='python3.5'
alias pip='pip3'

alias docker-quickstart='docker-machine start default; eval $(docker-machine env default)'

test -f $(brew --prefix)/etc/bash_completion && source $_

source ~/profile/common.bashrc

# Fix my broken umask
umask 002

