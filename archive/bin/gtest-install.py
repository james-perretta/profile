#! /usr/bin/python

import subprocess
from subprocess import call
from subprocess import check_call
from subprocess import CalledProcessError
import sys, os

install_dir = ''

if len(sys.argv) == 2:
    install_dir = sys.argv[1]
else:
    install_dir = '.'

os.chdir(install_dir)

try:
    if not os.path.exists('./gtest'):
        check_call(['svn', 'checkout', 
            'http://googletest.googlecode.com/svn/trunk/', 'gtest'])
    os.chdir('gtest/make')
    check_call('make')
    check_call('./sample1_unittest')
    print 'Installation successful'
except CalledProcessError as e:
    print e

