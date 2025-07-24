#! /usr/bin/env python

import sys

with open('.gitignore', 'a') as gitignore:
	for i in range(1, len(sys.argv)):
		gitignore.write(sys.argv[i] + '\n')
