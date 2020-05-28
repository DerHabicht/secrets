#!/usr/bin/env pipenv-shebang
"""Secrets

Tool for managing secrets drives.

Usage:
    secrets.py validate <dir>

Options:
    -h --help       Show this help message.
    --version       Print the version of this script.
"""
from docopt import docopt
from pprint import PrettyPrinter

VERSION = '0.1.0'
p = PrettyPrinter(indent=4)


if __name__ == '__main__':
    args = docopt(__doc__, version=VERSION)

    if args['validate']:


