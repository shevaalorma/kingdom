import datetime
import time

class TimeIt:
    def __init__(self, fn):
        self._fn = fn

    def __enter__(self):
        print('enter')
        self.start = datetime.datetime.now()
        return self

    def __call__(self, *args, **kwargs):
        return self._fn(*args,**kwargs)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        self.delta = (datetime.datetime.now() - self.start).total_seconds()
        print('context {} took {}s. context'.format(self.fn.__name__, self.delta))
        return



@TimeIt
def add(x, y):
    time.sleep(2)
    return x + y

print(add(4,5))
