import re

s = '''bottle\nbag\nbig\napple'''

for x in enumerate(s):
    if x[0] % 8 == 0:
        print()
        print(x,end=' ')
print('\n')

print('---match--')
result = re.match('b',s)
print(1,result)
result = re.match('a',s)
print(2,result)
result = re.match('^a',s,re.M)
print(3,result)
result = re.match('^a',s,re.S)
print(4,result)

regex = re.compile('a')
result = regex.match(s)
print(5,result)
result = regex.match(s,15)
print(6,result)
print()

print('--search--')
result = re.search('a',s)
print(7,result)
regex =re.compile('b')
result = regex.search(s,1)
print(8,result)
regex = re.compile('^b',re.M)
result = regex.search(s)
print(8.5,result)
result = regex.search(s,8)
print(9,result)


#fullmatch 方法
result = re.fullmatch('bag',s)
print(10,result)
regex = re.compile('bag')
result = regex.fullmatch(s)
print(11,result)
result = regex.fullmatch(s,7)
print(12,result)
result =regex.fullmatch(s,7,10)
print(13,result)

print('--------------------------------------')
# findall方法
result = re.findall('b',s)
print(1,result)
regex = re.compile('^b')
result = regex.findall(s)
print(2,result)
regex = re.compile('^b',re.M)
result = regex.findall(s,7)
print(3,result)
regex = re.compile('^b',re.S)
result = regex.findall(s)
print(4,result)
regex = re.compile('^b,re.M')
result = regex.findall(s,7,10)
print(5,result)

# #finditer方法
#
# result = regex.finditer(s)
# print(type(result))
# print(next(result))
# print(next(result))

#替换方法

regex = re.compile('b\wg')
result = regex.sub('magedu',s)
print(1,result)
result = regex.sub('magedu',s,1)
print(2,result)

regex = re.compile('\s+')
result = regex.subn('\t',s)
print(3,result)