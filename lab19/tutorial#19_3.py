import sys
import re

file_handler = open('lab19\\hosts.txt', "r")
general_lines = file_handler.readlines()
file_handler.close()

hosts = {}

for line in general_lines:
    key = re.search(r'^(.*)\=(.*)$', line).group(1)
    value = re.search(r'^(.*)\=(.*)$', line).group(2)
    hosts[key] = value

for i in sys.argv[1:]:
    try:
        print(hosts[i])
    except KeyError:
        print("invalid host name")

"""
Uri's comments:
==============

* Very good! This code works.
* It's better to put your data files (*.txt) in a separate folder and not with
  the code.
  
"""
