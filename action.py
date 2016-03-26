#!/usr/bin/python


from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import ssl

class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                maxsize=maxsize, 
                ssl_version=ssl.PROTOCOL_TLSv1)
        
import requests

s = requests.Session()
s.mount('https://', MyAdapter())


html = s.get("https://login.tikona.in/userportal/?requesturi=http%3a%2f%2f1%2e254%2e254%2e254%2f&ip=10%2e119%2e124%2e214&mac=c8%3a3a%3a35%3a2d%3a20%3a38&nas=tikonaokhlal3msc&requestip=1%2e254%2e254%2e254&sc=0885559aa94ef8f61b04d10cc2834578")

html2 = s.get('https://login.tikona.in/userportal/login.do?requesturi=http%3A%2F%2F1.254.254.254%2F&act=null')


print html2.text


