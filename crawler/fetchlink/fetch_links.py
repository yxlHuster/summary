#coding: utf-8

import re
import json
from utils import http_request
#from config import pattern
import pattern
from common.task import TaskConsumer, TaskProducer
from lcs import find_lcs
from common.logger import LoggerManager

class LinkFetcher(object):
    TASK_NAME = "spider_fetch_links"

    def __init__(self):
        self.producer = TaskProducer()
        self.consumer = TaskConsumer()
        self.consumer.register_task(LinkFetcher.TASK_NAME, self.process_job)

        self.logger = LoggerManager.get_logger(self.__class__.__name__)

    def fetch_links(self, host, type, url, is_page = None):
        if type in ['second', 'third']:
            return False, None

        code, content = http_request(url)
        if code != 200:
            return False, None

        content = content.decode('gbk', 'ignore').encode('utf-8')
        host_module = getattr(pattern, host)
        host_pattern = getattr(host_module, 'pattern', None)
        if not host_pattern:
            return False, None

        pdata = host_pattern.get(type, None)
        if pdata is None:
            return False, None

        links = []
        is_page = is_page if is_page is not None else pdata.get('is_pages', None)
        if is_page:
            page_links = self.get_link_list(pdata.get('pages_process'), content)
            page_num = self.get_pagenum(pdata['page_number'], content)

            if page_num > 2:
                template = self.get_template(page_links)
                links.extend([(host, type, template % i, False) for i in xrange(2, page_num + 1)])
            elif page_num == 2:
                links.append((host, type, page_links[0], False))

        for totype, cpattern in pdata.get('process').iteritems():
            linkre = re.compile(cpattern)
            links.extend([(host, totype, link.group(1), None) for link in linkre.finditer(content)])
        return True, links

    def process_split_pages(self, host, type, template, page_num):
        pass
    
    def get_link_list(self, pattern_, content):
        pre = re.compile(pattern_)
        return pre.findall(content)

    def get_pagenum(self, pattern_, content):
        pre = re.compile(pattern_)
        numbers = pre.findall(content)

        if len(numbers) <= 0:
            return 0

        number = int(numbers[0])
        return number

    def get_template(self, templates):
        lcs_str = find_lcs(templates[0], templates[1])
        t = []

        for i, x in enumerate(templates[0]):
            if lcs_str[i] != x:
                break
            t.append(x)
        t.append("%d")
        t.append(lcs_str[i:])
        return ''.join(t)

    def process_job(self, consumer, job):
        items = json.loads(job.data)
        if items['type'] == 'third':
            return True

        rc, links = self.fetch_links(items['host'], items['type'], items['url'], items.get('is_page', None))
        if not rc:
            self.logger.warn("[SPIDER_FETCH_LINKS] Process fetch links Error, %s" % (job.data))
            return False

        for host, type, url, is_page in links:
            if type == 'third':
                continue
            self.logger.debug("%s\t%s\t%s\t%s" % (host, type, url, is_page))
            self.producer.submit_job(LinkFetcher.TASK_NAME, json.dumps({'host': host, 'type': type, 'url': url, 'is_page': is_page}))
        return True

    def start(self):
        self.consumer.run()

if __name__ == '__main__':
    fetcher = LinkFetcher()
    fetcher.start()
