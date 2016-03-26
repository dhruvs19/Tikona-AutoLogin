#!/usr/bin/python

import requests
import sys
import re

url = requests.get("http://1.254.254.254")


statuscode = url.status_code

if statuscode == 200:
	print "page received sucessfully"
else:
	print "Error Loading the page.. Exiting"
	sys.exit(0)

arr = re.search('requesturi.*',url.text).group(0)
	
print 'https://login.tikona.in/userportal/?'+arr[0:-2]

