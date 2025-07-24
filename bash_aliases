profile_dir=$(dirname $(realpath "$BASH_SOURCE"))

alias refresh-profile='source ~/.bashrc'

alias ls="ls --color=auto -Fh"
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -la'

alias grep='grep --colour=auto'

# Automatically run 'ls' after changing directory.
function cd() {
    builtin cd "$@" && ls;
}

# Navigate up one directory. This is here instead of in aliases
# so that it uses the above overload of cd.
function up() {
    cd ..
}

function upup() {
    cd ../..
}

function upupup() {
    cd ../../..
}

# Print one arg per line
function pr() {
    printf "%s\n" "$@"
}

# ==================== SAFETY =======================

function rm () {
    echo "I don't think you really want to do that"
}

# ==================== SSH =======================

function sshbee() {
    num=$1
    shift
    ssh "agworker$num.eecs.umich.edu" $@
}

function sshstage() {
    num=$1
    shift
    ssh "autograder@ag-staging-$num.eecs.umich.edu" $@
}

# ==================== GIT =======================

source $profile_dir/git.git-completion.bash

alias gs='git status'
alias ga='git add'
alias gau='git add -u'
alias gc='git commit -m'
alias gp='git push'
alias gpl='git pull'
alias gfo='git fetch origin'

function gitignore() {
    printf "%s\n" "$@" >> .gitignore
}

function git-unpublish() {
    for arg in "$@"
    do
        git push origin :"$arg"
    done
    git status;
}

# ==================== PYTHON =======================

# Create a global Python Virtual environment
_python_venvs_home=$HOME/python_venvs
function create_venv() {
    mkdir -p $_python_venvs_home
    python3 -m venv $_python_venvs_home/$1
}

function activate()  {
    source $1/bin/activate
}

# Activate the specified global Python Virtual environment
function gactivate() {
    source $_python_venvs_home/$1/bin/activate
}
_gactivate() {
    COMPREPLY=()
    COMPREPLY=$(/bin/ls $_python_venvs_home | tr "\n " " ")
}
complete -F _gactivate gactivate
