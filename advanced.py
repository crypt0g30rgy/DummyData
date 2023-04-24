#!/usr/bin/env python3

import re
import requests

url = "https://forebears.io/kenya/forenames"

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36' }

proxies = {'http' : 'http://127.0.0.1:8080'}

response = requests.get(url,headers=headers, proxies=proxies)

html = response.content.decode('utf-8')

regex = r'<a href="forenames/([^"]+)">([^<]+)</a>'

matches = re.findall(regex, html)

for match in matches:
    value = match[1]
    print(value)
