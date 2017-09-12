#!/usr/bin/env python3
import urllib.parse
import urllib.request
import sys
import os
import xml.etree.ElementTree as ET
def getwolfram(query):
    query = urllib.parse.quote(query)
    appid = os.environ['WOLFRAM_ALPHA_V2_APP_ID']
    response = urllib.request.urlopen('https://api.wolframalpha.com/v2/query?appid=' + appid + '&input=' + query)
    content = response.read().decode('utf-8')
    return ET.fromstring(content)[0][0][1].text

if __name__ == '__main__':
    print(getwolfram(' '.join(sys.argv[1:])))

