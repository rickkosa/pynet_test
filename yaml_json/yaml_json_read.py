#!/usr/bin/python

import yaml
import json

with open("ex6.yml") as f:
    f_yml = yaml.load(f)
    print yaml.dump(f_yml, default_flow_style=False)

with open("ex6.json") as f:
    f_json = json.load(f)
    print json.dumps(f_json, indent=4)
