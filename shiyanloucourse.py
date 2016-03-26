#coding:utf8
import urllib
import re
html = 'http://www.shiyanlou.com/courses/'

for i in range(10):
    htm = html + str(i)
    print htm
    page = urllib.urlopen(htm)
    sea = re.search(r'<title>(.*)</title>', page.read())
    
    print i,sea.group(0)
