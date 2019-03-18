#!/usr/bin/env python

import urllib2
import sys
import json

data = urllib2.urlopen(sys.argv[1])
json_data = json.loads(data.read())
fichier = open("json.txt", "wb")
fichier.write(str(json_data))
fichier.close()

