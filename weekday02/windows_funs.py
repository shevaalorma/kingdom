import random
import datetime
import time


def sorce():
    while True:
        {'value':random.randint(1,100),'datetime':datetime.datetime.now()}
        time.sleep(1)

def window(src,handler,width:int,interval:int):
    '''
    窗口函数
    :param src: 数据源，生成器，用来那数据
    :param handler: 数据处理函数
    :param width: 数据窗口函数，秒
    :param interval: 处理时间间隔，秒
    '''
    start =datetime.datetime.strptime('20170101 01:00:00 +0800','%Y%m%d %H:%M:%S %z')
    current =datetime.datetime.strptime('20170101 01:00:00 +0800','%Y%m%d %H:%M:%S %z' )

