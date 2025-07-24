# If not running interactively, don't do anything
[ -z "$PS1" ] && return

alias ls='ls --color=auto -F' # color works on linux but not on mac

source ~/profile/common.bashrc

echo 'Loading caen settings...'

#PYTHONPATH=$PYTHONPATH:~/python2.7/bin
PYTHON_2_7=~/opt/python2.7/bin
PYTHON_3_4=~/opt/python3.4/bin
#SUBMIT_381=/afs/umich.edu/class/eecs381/bin
export PATH=$PYTHON_2_7:$PYTHON_3_4:$PATH:~/bin-caen:$SUBMIT_381

# module load gcc/4.7.0
module load gcc/4.8.2

#export PATH=$PATH:/afs/umich.edu/class/eecs280

#PATH=/usr/um/gcc-4.7.0/bin:$PATH
#LD_LIBRARY_PATH=/usr/um/gcc-4.7.0/lib64
#LD_RUN_PATH=/usr/um/gcc-4.7.0/lib64

function backup()
{
	dest="$HOME/backup/${PWD##*/}/$(date +"%m-%d-%Y--%I:%M:%S-%p")"
	mkdir -p "$dest"
	cp -i -r -t "$dest" "$@"
}
