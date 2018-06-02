import datetime

log_line = '''183.60.212.153 – – [19/Feb/2013:10:23:29 +0800] \
“GET /o2o/media.html?menu=3 HTTP/1.1” 200 16691 “-” \
“Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)”'''


def extract(line):

    lst = []
    tmp = ''
    flag = False

    names = ["remote","","","datetime","request","status","length","","useragent"]

    ops = [None,None,None,lambda timestr:datetime.datetime.strptime(timestr,'%d/%b/%Y:%H:%M:%S %z'),lambda request:dict(zip(("Method","url","protocol"),request.split())),int,int,None,None]


    for word in line.split():
        #print(word)
        if not flag and (word.startswith("[") or word.startswith('“')):
            if word.endswith("]") or word.endswith("”"):
                lst.append(word.strip("[]“”"))
            else:
                tmp += word[1:]
                flag = True
            continue
        if flag:
            if word.endswith("]") or word.endswith("”"):
                tmp += " " + word[:-1]
                lst.append(tmp)
                flag = False
                tmp = ''
            else:
                tmp += ' ' + word
            continue
        lst.append(word)
    #print(lst)

    d = {}
    for i,v in enumerate(lst):
            key = names[i]
            if ops[i]:
                d[key] = ops[i](v)
            d[key] = v
    return d


print(extract(log_line))




