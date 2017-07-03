#! usr/bin/python
# cording:utf-8
import redis
r=redis.Redis(host="127.0.0.1",port="6379",password="123456")
r.set("testComm","33333")
print(r.get("testComm"))