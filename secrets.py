#!/usr/bin/env pipenv-shebang
"""Secrets

Tool for managing secrets drives.

Usage:
    secrets.py validate <manifest>

Options:
    -h --help       Show this help message.
    --version       Print the version of this script.
"""
import json
import yaml
from docopt import docopt
from jsonschema import validate
from os import getcwd
from os.path import abspath, dirname


VERSION = '0.1.0'


def validate_manifest(m):
    with open(f'{dirname(abspath(__file__))}/schema.json', 'r') as f:
        schema = json.loads(f.read())

    with open(f'{getcwd()}/{m}', 'r') as f:
        manifest = yaml.safe_load(f.read())

    validate(manifest, schema)


if __name__ == '__main__':
    args = docopt(__doc__, version=VERSION)

    if args['validate']:
        validate_manifest(args['<manifest>'])

