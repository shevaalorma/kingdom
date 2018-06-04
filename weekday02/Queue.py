from  queue import Queue

import random

q = Queue()

q.put(random.randint(1,100))
q.put(random.randint(1,100))

print(q.get())
print(q.get())
print(q.get())
#print(q.get(timeout=3))

import threading

t = threading.Thread(target=window,args=(src,hanler,width,interval))

t.start()