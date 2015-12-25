#-*-coding:utf-8-*-

import traceback
from lib.gearman.worker import GearmanWorker
from lib.gearman.client import GearmanClient
from common.config import task_server_list
from common.logger import LoggerManager

class TaskProducer(object):

    def __init__(self):
        self.client = GearmanClient(task_server_list)

    def submit_job(self, queue, data):
        self.client.submit_job(queue, data, background = True)


class TaskConsumer(object):

    def __init__(self):
        self.worker = GearmanWorker(task_server_list)
        self.logger = LoggerManager.get_logger(self.__class__.__name__)
    
    def register_task(self, queue, callback):
        def wrapper(worker, job):
            try:
                rc = callback(self, job)
                if not rc:
                    self.logger.error('[TASK_CONSUMER] TaskConsumer process job error, task: %s, job: %s' % (job.task, job.data))
                return "TRUE" if rc else "FALSE"
            except:
                print traceback.format_exc()
                self.logger.error('[TASK_CONSUMER] TaskConsumer process job error, task: %s, job: %s' % (job.task, job.data))
                return "FALSE"
        self.worker.register_task(queue, wrapper)

    def unregister_task(self, queue):
        self.worker.unregister_task(queue)

    def run(self):
        while True:
            self.worker.work()

    def ack(self, job):
        pass

    def failed(self, job):
        self.worker.send_job_failure(job)
        print "[JOB_FAIL] task: %s, data: %s" % (job.task, job.data)
