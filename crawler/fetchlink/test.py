#coding: utf-8

import re
import json
from utils import http_request
import pattern

#code, content = http_request("http://bbs.wdzj.com/forum-2-1.html")
#content = content.decode('gbk', 'ignore').encode('utf-8')

#sre = re.compile('<h2><a href="([^\"]+)"  style="">[^<]+</a>')
#for x in sre.finditer(content):
#    print x.group(1)
#
#print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
#print content 

#rre = re.compile('<a href="[^\"]+" onclick="atarget\(this\)" class="s\sxst">[^\<]+</a>')
#for x in rre.finditer(content):
#    print x.group(0)

# pagere = re.compile('<span id="fd_page_bottom"><div class="pg">([\s\S]+?)</div>')
# x = pagere.findall(content)

# linkre = re.compile('<a href="([^\"]+)">[\d]+</a>')
# pre = None
# #from lcs import find_lcs
# for x in linkre.findall(content):
#     print x
#     #if pre:
#     #    print find_lcs(pre, x)
# 
#     pre = x
# 
# pagenum = re.compile('<span title="共[\s]+([\d]+) 页"> /[\s]+[\d]+[\s]+页</span>')
# x = pagenum.findall(content)
# print x

print getattr(pattern, 'wdzj')
