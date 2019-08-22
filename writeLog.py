'''
Created on 2019年8月13日

@author: JinLian
'''
import logging
# 创建一个日志记录器 logger
logger = logging.getLogger('mylogger')  # 参数为 日志记录器名称
logger.setLevel(logging.DEBUG)  # 设置日志记录器的级别
print(logger.name, logger.parent, type(
    logger), id(logger), id(logger.parent))
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')  # 参数为 日志文件名称
fh.setLevel(logging.CRITICAL)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(levelno)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('开始打印日记')
