# If not running interactively, don't do anything
[ -z "$PS1" ] && return

lsflags='--color=auto'
alias grep='grep --colour=auto'
export PS1="\u \w $ "

echo 'Loading my ubuntu settings...'

# Dart binaries
PATH=/usr/lib/dart/bin:$PATH

alias python='python3'

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

source ~/profile/common.bashrc
#source ~/profile/color.bashrc


export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

alias nvpn='globalprotect connect -portal vpn.northeastern.edu'

