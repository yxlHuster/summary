#-*-coding:utf-8-*-

import logging
from common.config import DEBUG

class LoggerManager(object):
    _instance = None

    def __init__(self):
        
        self.handler = None
        if DEBUG:
            self.handler = logging.StreamHandler()
        else:
            self.handler = loggin.FileHandler('/tmp/spider.log')
        
        formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(formatter)
        self.handler.setFormatter(self.formatter)

    @staticmethod
    def get_instance():
        if LoggerManager._instance == None:
            LoggerManager._instance = LoggerManager()
        return LoggerManager._instance
    
    @staticmethod 
    def get_logger(name):
        ins = LoggerManager.get_instance()
        logger = logging.getLogger(name)
        logger.addHandler(ins.handler)
        logger.setLevel(logging.DEBUG)
        return logger


if __name__ == "__main__":
    logger1 = LoggerManager.get_logger('1')
    logger1.debug('Debug')

    logger2 = LoggerManager.get_logger('2')
    logger2.info('debug')

