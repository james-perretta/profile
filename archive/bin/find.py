#! /usr/bin/env python

import os
import argparse

from fnmatch import fnmatch


def main():
    args = parse_args()

    not_found = True
    for root, dirnames, filenames in os.walk(args.starting_directory):
        for item in dirnames + filenames:
            if fnmatch(item, args.what_to_find):
                print("Found: " + os.path.join(root, item))
                not_found = False

        if args.shallow:
            break

    if not_found:
        print('Search query "' + args.what_to_find + '" yielded no results.')

# -----------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("what_to_find",
        help="A file/directory name or a shell pattern")
    parser.add_argument("--starting_directory", "-s", default=os.getcwd(),
        help="The directory in which to start the search. Defaults to the current working directory.")
    parser.add_argument("--shallow", action='store_true', default=False,
        help="Only search the starting directory.")

    return parser.parse_args()

if __name__ == '__main__':
    main()
