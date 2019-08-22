'''
Created on 2019年8月19日

@author: JinLian
'''
import logging
from logging.handlers import RotatingFileHandler  # 日志回滚类

# 设置日志输出到控制台的格式
logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s -%(name)s- %(levelname)s - %(message)s - %(relativeCreated)d')

# 创建一个日志记录器
log1 = logging.getLogger('s')
# log1.setLevel(logging.INFO)
print(1, log1.getEffectiveLevel())

# 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
ro = RotatingFileHandler('log.txt', maxBytes=1 * 1024, backupCount=3)
ro.setLevel(logging.INFO)
formatro = logging.Formatter(
    '%(asctime)s -%(filename)s - %(levelno)s -%(message)s')
ro.setFormatter(formatro)

# 创建一个日志输出文件
h1 = logging.FileHandler('h1.log')
# 设置 文件接收日志级别
h1.setLevel(logging.CRITICAL)
# 设置输入到文件格式
formatter = logging.Formatter('%(asctime)s - %(levelno)s -%(message)s')
print(2, h1.level)
# 把定义好的格式加到 文件对象
h1.setFormatter(formatter)

# 把文件对象 加到 日志记录器
log1.addHandler(h1)
log1.addHandler(ro)
# 把要输出的信息 写入 日志记录器
log1.critical('开始记录日志 ' + ' - 记录器级别' + str(log1.getEffectiveLevel()))
