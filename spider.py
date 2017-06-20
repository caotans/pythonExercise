#!/usr/bin/env python
#coding=utf-8
import urllib.request
import re
url="https://www.qiushibaike.com/" #糗事百科网址
#抓取过程
config=urllib.request.Request(url)
config.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")
config.add_header("Refer","eclick.baidu.com")#伪装成百度知道访问过来的
#访问其中一个页面的数据
request=urllib.request.urlopen(config)
respones=request.read()
data=respones.decode("utf8")#解码成utf8
request.close()
patten=re.compile("<span>.*?</span>",re.S)
print(re.findall(patten,data))


