import inspect

def logger(fn,*args,**kwargs):
    def wrapper(*args,**kwargs):
        print("begin")
        x = fn(*args,**kwargs)
        sig = inspect.signature(fn)
        od = sig.parameters()
        param_list = list(od.keys())
        print(param_list)
        print("end")
        return x
    return wrapper

@logger
def add(x,y=5):
    return x + y

print(add(5))