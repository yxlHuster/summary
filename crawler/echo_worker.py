#coding: utf-8

import sys
print sys.path
from common.task import TaskConsumer

def echo(consumer, job):
    print job.data
    return "TRUE"

consumer = TaskConsumer()
consumer.register_task('spider_fetch_links', echo)
consumer.run()
