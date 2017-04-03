#!/usr/bin/python

import yaml
import json

my_list = range(8)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]
my_list[-1]['ip_addr'] = '10.10.10.239'
my_list[-1]['attribs'] = range(7)

with open("ex6.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open("ex6.json", "w") as f:
    f.write(json.dumps(my_list)) 
