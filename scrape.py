#!/usr/bin/env python3

import re
import requests

url = "https://studentsoftheworld.info/penpals/stats.php?Pays=KEN"
response = requests.get(url)
html = response.content.decode('utf-8')

pattern = r'<FONT class=text2>(.*?)</TD>'
matches = re.findall(pattern, html, re.DOTALL)

for match in matches:
    print(match)
