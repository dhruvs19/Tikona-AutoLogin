#!/usr/bin/python

import requests

url = requests.get("http://1.254.254.254")

print url.text
input