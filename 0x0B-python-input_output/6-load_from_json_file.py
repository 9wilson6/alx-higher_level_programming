#!/usr/bin/python3

""" create an object from JSON file """

import json

def load_from_json_file(filename):
    """ create object from filename """

    with open(filename, 'r') as f:
        return json.load(f)
