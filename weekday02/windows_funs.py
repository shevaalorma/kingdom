import random
import datetime
import time


def source():
    while True:
        yield {'value': random.randint(1, 100), 'datetime': datetime.datetime.now()}
        time.sleep(1)


def window(src, handler, width: int, interval: int):
    '''
    窗口函数
    :param src: 数据源，生成器，用来那数据
    :param handler: 数据处理函数
    :param width: 数据窗口函数，秒
    :param interval: 处理时间间隔，秒
    '''
    start = datetime.datetime.strptime('20170101 00:00:00 +0800', '%Y%m%d %H:%M:%S')
    current = datetime.datetime.strptime('20170101 01:00:01 +0800', '%Y%m%d %H:%M:%S')

    buffer = []
    delta = datetime.timedelta(seconds=width - interval)

    while True:
        #
        data = next(src)
        if data:
            buffer.append(data)
            current = data['datetime']

        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            print("{:.2f}".format(ret))
            start = current

            buffer = [x for x in buffer if x['datetime'] > current - delta]


def handler(iterable):
    vals = [x['value'] for x in iterable]
    return sum(vals) / len(vals)


window(source(), handler, 10, 5)
