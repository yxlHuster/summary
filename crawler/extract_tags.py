#-*-coding:utf-8-*-

import re
import sys


def extract(path):
    pattern = re.compile('<li class="transition"><a href="/tags/(\\d+).html">(.*?)</a></li>')
    with open(path) as f:
        content = f.read()
        foundTags = re.findall(pattern, content)
        for tag in foundTags:
            print tag[1]

extract(sys.argv[1])
        







