#!/usr/bin/env python
#coding=utf-8
import urllib.request
url="http://www.baidu.com"
request=urllib.request.Request(url)
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")
r=urllib.request.urlopen(request)
response=r.read()
mystr = response.decode("utf8")
r.close()
print(mystr)
