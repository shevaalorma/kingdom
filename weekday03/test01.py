import datetime
import time
from functools import wraps

def magedu(fn):
    @wraps(fn)
    def warpper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        print(datetime.datetime.now()-start)
        return ret
    return warpper

@magedu #add = magedu(add)
def add(x,y):
    time.sleep(2)
    return x + y

print(add(40,50))

