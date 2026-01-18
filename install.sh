#! /bin/bash

set -e

profile_dir=$(dirname $(realpath "$0"))

ln -s $profile_dir/bash_aliases ~/.bash_aliases
