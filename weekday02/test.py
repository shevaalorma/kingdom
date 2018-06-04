import random
import datetime
import time
from queue import Queue
import threading


def source():
    yield {'value':random.randint(1,100),'datetime':datetime.datetime.now()}
    time.sleep(1)


def windows(src:Queue,handler,width:int,interval:int):
    start = datetime.datetime.strptime('2017-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
    current = datetime.datetime.strptime('2017-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(seconds= width - interval)
    buffer = []
    for data in src.get():
        if data:
            buffer.append(data)
            current = data['datetime']

        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            print("{:.2f}".format(ret))
            current = start

        buffer =[x for x in buffer if x['datetime'] >  current -delta ]


def handler(iterable):
    vals = [x['value'] for x in iterable]
    return sum(vals) / len(vals)

def dispatcher(src):
    queues = []
    handlers = []
    def reg(handler,width,interval):
        q = Queue()
        queues.append(q)

        h = threading.Thread(target=windows,args=(q,width,interval))
        handler.append(h)

    def run():
        for t in handlers:
            t.start()
        for item in src:
            for q in queues:
                q.put(item)
    return reg,run

reg ,run = dispatcher(source())

run()



#windows(source(),handler,10,5)
