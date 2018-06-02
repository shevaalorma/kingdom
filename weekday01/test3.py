soure = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
target = {}

def flatmap(src,prefix = ''):
    for k,v in src.items():
        if isinstance(v,(set,tuple,list,dict)):
            flatmap(v,prefix = prefix + k +'.')
        else:
            target[prefix+k] = v

flatmap(soure)
print(target)