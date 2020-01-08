# 编写初始化日志的函数

import logging
from logging import handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = 'http://182.92.81.159'
HEADERS = {'Content-Type': 'application/json'}
EMP_ID = ''


def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)  # setLevel里面是整型
    # 设置处理器（2个）
    sh = logging.StreamHandler()  # 设置控制台处理器
    filename = BASE_DIR + '/log/ihrm.log'  # 日志所在目录以及名称,__file__是所在文件的绝对路径，现在在app.py，就是app.py的绝对路径
    fh = logging.handlers.TimedRotatingFileHandler(filename, when='M', interval=1,
                                                   backupCount=7)  # 设置文件处理器,Time可以用来切分日志，时间切分生成日志
    # 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)
