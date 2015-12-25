#coding: utf-8

import json
from common.task import TaskProducer

client = TaskProducer()
client.submit_job('spider_fetch_links', json.dumps({'host': 'wdzj', 'type': 'entry', 'url': 'http://bbs.wdzj.com/forum-2-1.html'}))
