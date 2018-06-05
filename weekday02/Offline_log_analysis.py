import random
import datetime
import time
from queue import Queue
import threading
import re
import logging


log_line = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

def extract(line) -> dict:
    names = ["remote", "", "", "datetime", "request", "status", "length", "", "useragent"]
    ops = {'datetime':lambda timestr:datetime.datetime.strptime(timestr,"%d/%b/%Y:%H:%M:%S %z"),
           'status': int,
           'length': int}

    pattern_str = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[/\w +:]+)\] "(?P<method>\w+) (?P<url>\S+) (?P<protocol>[\w/.]+)" (?P<status>\d+) (?P<length>\d+) "[^"]+" "(?P<userangent>[^"]+)"'''
    regex = re.compile(pattern_str)

    matcger = regex.match(line)
    info ={k:ops.get(k,lambda x:x)(v) for k,v in matcger.groupdict().items()}
    #print(info)
    return info

def load(path):
    with open(path) as f:
        for line in f:
            fileds = extract(line)
            if fileds:
                yield fileds
            else:
                continue

def source():
    yield {'value':random.randint(1,100),'datetime':datetime.datetime.now()}
    time.sleep(1)


def windows(src:Queue,handler,width:int,interval:int):
    start = datetime.datetime.strptime('2017-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
    current = datetime.datetime.strptime('2017-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(seconds= width - interval)
    buffer = []
    while True:
        data = src.get()
        if data:
            buffer.append(data)
            current = data['datetime']

        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            print("{:.2f}".format(ret))
            current = start

        #重叠方案
        buffer =[x for x in buffer if x['datetime'] > current -delta ]


def handler(iterable):
    vals = [x['value'] for x in iterable]
    return sum(vals) / len(vals)

def dispatcher(src):
    queues = []
    handlers = []
    def reg(handler,width,interval):
        q = Queue()
        queues.append(q)

        h = threading.Thread(target=windows,args=(q,handler,width,interval))
        handlers.append(h)

    def run():
        for t in handlers:
            t.start()
        for item in src:
            for q in queues:
                q.put(item)
    return reg,run

def donothing_handler(iterable):
    return iterable


if __name__=="__main__":
    import sys
    path = 'test.log'
    #字典
    reg, run = dispatcher(load(path))
    reg(donothing_handler,10,5)
    run()
    logging.info()

