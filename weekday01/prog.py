from os import path

p = path.join('/etc','sysconfig','network')
print(type(p),p)
print(path.exists(p))
print(path.split(p))
print(path.abspath('.'))

print('________________________________________')

p = path.join('e:/',p,'test.txt')
print(path.dirname(p))
print(path.basename(p))
print(path.splitdrive(p))

from  pathlib import Path

print('________________________________________')

p = Path()
p = Path('a','b','c/d')
p = Path('/etc')

print('________________________________________')

p = Path()
p = p / 'a'
print(p)