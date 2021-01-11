# coding:utf-8

import logging
import os
from config.constans import DEFAULT_SERVICE_NAME


class LogModule:

    def __init__(self):
        self.logger = logging.getLogger(DEFAULT_SERVICE_NAME)
        self.logger.setLevel(logging.DEBUG)  # Log等级总开关

        logfile = os.path.join('log', 'mainlog.log')
        if not os.path.exists(logfile):
            os.mkdir(os.path.join(os.getcwd(),'log'))

        if not self.logger.handlers: #  句柄只需要创建一次，相当于是个单例效果
            fh = logging.FileHandler(logfile, mode='a')
            fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关

            #  创建一个输入流到ELK
            pass

            '''
            %(levelno)s：打印日志级别的数值
            %(levelname)s：打印日志级别的名称
            %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
            %(filename)s：打印当前执行程序名
            %(funcName)s：打印日志的当前函数
            %(lineno)d：打印日志的当前行号
            %(asctime)s：打印日志的时间
            %(thread)d：打印线程ID
            %(threadName)s：打印线程名称
            %(process)d：打印进程ID
            %(message)s：打印日志信息
            '''
            fmt = logging.Formatter("%(asctime)s - %(name)s[line:%(lineno)d] - %(levelname)s: %(message)s")
            fh.setFormatter(fmt)
            ch.setFormatter(fmt)

            self.logger.addHandler(fh)
            self.logger.addHandler(ch)


    def debug(self, msg, **args):
        self.logger.debug(msg)

    def warn(self, msg, **args):
        self.logger.warning(msg)

    def warning(self, msg, **args):
        self.logger.warning(msg)

    def error(self, msg, **args):
        self.logger.error(msg)

    def info(self, msg, **args):
        self.logger.info(msg)

    def write_log(self, msg='', **args):
        pass

    def getFileLog(self):
        return self
