import random
import datetime
import time


def source():
    while True:
        yield {'value' : random.randint(1,100),'datetime':datetime.datetime.now()}
        time.sleep(1)


#获取数据
s = source()
items = [next(s) for _ in range(3)]

#处理函数
def handler(iterable):
    vals = [x['value'] for x in iterable]
    return sum(vals) / len(vals)

print(items)
print("{:.2f}".format(handler(items)))