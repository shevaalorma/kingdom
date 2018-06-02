import inspect
import datetime
import time
from functools import wraps

def mag_cache(duration):
    def _cache(fn):
        lru_cache = {}
        @wraps(fn)
        def wrapper(*args, **kwargs):
            def clear_expire(cache):
                expire = []
                for i,(_,stamp) in cache.items():
                    now = datetime.datetime.now().timestamp()
                    if now - stamp > duration:
                        expire .append(i)

                for k in expire:
                        lru_cache.pop(k)

            clear_expire(lru_cache)
        # print(keys,lru_dict,end="\n\n")
        # 判断是否有缓存


            def make_key():
                sig = inspect.signature(fn)
                parms = sig.parameters  # od
                parms_list = list(parms.keys())  # od_keys
                lru_dict = {}
                # 位置参数
                for i, v in enumerate(args):
                    k = parms_list[i]
                    lru_dict[k] = v
                # 关键字参数
                lru_dict.update(kwargs)
                # 默认值
                for k, v in parms.items():
                    if k not in lru_dict.keys():
                        lru_dict[k] = v.default
                return tuple(sorted(lru_dict.items()))
            keys = make_key()

            if keys not in lru_cache.keys():
                lru_cache[keys] = (fn(*args, **kwargs), datetime.datetime.now().timestamp())
            return keys, lru_cache
        return wrapper
    return _cache

def logger(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta =(datetime.datetime.now()-start).total_seconds()
        print(fn.__name__,delta)
        return ret
    return wrapper

@logger
@mag_cache(5)
def add(x,y=10):
    time.sleep(3)
    return x + y

add(4)
time.sleep(4)
add(4,10)
add(x=4,y=10)
add(y=10,x=4)
