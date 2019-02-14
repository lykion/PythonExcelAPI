# -*- coding:utf-8 -*-
import logging
import logging.handlers
import time


class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger()   # 创建一个logger
        self.logger.setLevel(logging.INFO)  # logger等级总开关

        # 定义log的输出格式
        self.formatter = logging.Formatter(
            '[ %(asctime)s ]--%(threadName)-10s %(thread)d  line:%(lineno)d  [%(levelname)s] *** '
            '%(message)s',
            '%Y-%m-%d %H:%M:%S')

        '''创建一个handler输出到文件'''
        t = time.localtime()    # 获取本地时间
        now = time.strftime("%Y%m%d%H%M%S", t)  # 转化时间格式
        # self.logfile = logging.FileHandler('test_'+now+'.log', encoding='UTF-8')    # 以转换的时间来命名log文件
        # self.logfile.setFormatter(self.formatter)
        # self.logfile.setLevel(logging.INFO)
        # self.logger.addHandler(self.logfile)
        '''
        为了避免log文件中出现重复打印，在handler前面加一个判断，如果已经有handler了，则不再添加handler
        '''
        if not self.logger.handlers:
            self.logfile = logging.FileHandler('test_'+now+'.log', encoding='UTF-8')
            self.logfile.setFormatter(self.formatter)
            self.logfile.setLevel(logging.INFO)
            self.logger.addHandler(self.logfile)

        '''创建一个handler，用于输出到控制台'''
        self.consle = logging.StreamHandler()
        self.consle.setFormatter(self.formatter)
        self.consle.setLevel(logging.INFO)

        self.logger.addHandler(self.consle)

    '''
    1、使用removeHandler()方法可以解决重复打印的问题
    2、会出现重复打印的原因在于：logger封装好后，调用的时候，会根据getLogger(name)里的name获取同一个logger，但是这个logger里已经有了之前添加的handler了，
       再次调用时又会添加一个handler。所以，这个logger里面就会又多了一个handler，依次类推，调用几次就会有几个handler
    3、针对重复打印的问题，提出4个解决方法：（感谢强大的网民^-^）
    ① 每次创建不同name的logger，这样每次都是新的logger，就不会添加多个handler了（ps：该方法不推荐）
    ② 每次用完logger后，使用removeHandler()把logger里面的handler移除掉
    ③ 在使用logger之前，进行判断，如果已经有handler了，就不在添加了 （ps：推荐使用此种方法）
    ④ 每次使用完logger后，使用pop()把logger列表的handler移除
    '''
    # 日志的5个级别对应的5个函数
    def debug(self, msg):
        self.logger.debug(msg)
        self.logger.removeHandler(self.consle)

    def info(self, msg):
        self.logger.info(msg)
        self.logger.removeHandler(self.consle)

    def warn(self, msg):
        self.logger.warning(msg)
        self.logger.removeHandler(self.consle)

    def error(self, msg):
        self.logger.error(msg)
        self.logger.removeHandler(self.consle)

    def critical(self, msg):
        self.logger.critical(msg)
        self.logger.removeHandler(self.consle)


if __name__ == '__main__':
    log = Logger()
    log.info(12452)
    log.error('d4e4f52d12')
    # Logger('1').info(45454)
    # Logger('2').error(122)
