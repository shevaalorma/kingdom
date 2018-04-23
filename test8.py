import datetime

log_line = '''183.60.212.153 – – [19/Feb/2013:10:23:29 +0800] \
“GET /o2o/media.html?menu=3 HTTP/1.1” 200 16691 “-” \
“Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)”'''


lst = []
tmp = ''
flag = False #用来判断 块语句

for word in log_line.split():
    #print(word)
    if not flag and (word.startswith('[') or word.startswith('“')):
        if word.endswith("]") or word.endswith('”'):
            lst.append(word.strip('“”[]'))
        else:
            tmp += ' ' + word[1:]
            flag = True
        continue


    if flag:
        if word.endswith("]") or word.endswith('”'):
            tmp += ' ' + word[:-1]
            flag = False
            lst.append(tmp)
            tmp = ''

        else: # 没找到后括号处理
            tmp += ' ' + word
        continue
    lst.append(word)

names = ["remote", "", "", "datetime", "request", "status", "length", "", "useragent"]

ops = [None, None, None,lambda timestr:datetime.datetime.strptime(timestr," %d/%b/%Y:%H:%M:%S %z"),lambda request: dict(zip(("Method", "url", "protocol"), request.split())), int, int, None, None]

print(lst)

d = {}
for i,v in enumerate(lst):
    #print(i,v)
    key = names[i]
    if ops[i]:
        d[key] = ops[i](v)
    d[key] = v


print(d)
