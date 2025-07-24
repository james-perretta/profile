#! /usr/bin/env python

import sys
import argparse
from subprocess import call


def main():
    # if len(sys.argv) != 2:
    #    print("Error: Usage: ./{0} [new-url]")
    args = parse_args()
    print(["git", "remote", "set-url", "origin", args.new_url])


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("new_url")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
