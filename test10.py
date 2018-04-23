import re
s = '''01 bottle
02 bag
03       bag1
100         able'''

for x in enumerate(s):
    if x[0] % 8 == 0:
        print()
    print(x,end=' ')

print()
print(0,s.split())
result = re.split('[\s\d]+',s)
print(1,result)
regex = re.compile('^[\s\d]+')
result = regex.split(s)
print(2,result)
regex = re.compile('^[\s\d]+',re.M)
result = regex.split(s)
print(3,result)
regex = re.compile('\s+\d+\s+')
result = regex.split(' '+s)
print(4,result)

#分组