import json
import jsonschema
import yaml
from os.path import abspath, dirname


class Manifest(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!Manifest'


def validate(manifest):
    with open(f'{dirname(abspath(__file__))}/schema.json', 'r') as f:
        schema = json.loads(f.read())

    with open(manifest, 'r') as f:
        manifest = yaml.safe_load(f.read())

    jsonschema.validate(manifest, schema)


