import datetime
import re

log_line = '''183.60.212.153 - - [19/Feb/2013:10:23:29 +0800] "GET /o2o/media.html?menu=3 HTTP/1.1" 200 16691 "-" "Mozilla/5.0 (compatible; EasouSpider; +http://www.easou.com/search/spider.html)"'''

def extract(line):
    names = ["remote", "", "", "datetime", "request", "status", "length", "", "useragent"]
    ops = {'datetime':lambda timestr:datetime.datetime.strptime(timestr,"%d/%b/%Y:%H:%M:%S %z"),
           'status': int,
           'length': int}

    pattern_str = '''(?P<remote>[\d.]{7,}) - - \[(?P<datetime>[/\w +:]+)\] "(?P<method>\w+) (?P<url>\S+) (?P<protocol>[\w/.]+)" (?P<status>\d+) (?P<length>\d+) "[^"]+" "(?P<userangent>[^"]+)"'''
    regex = re.compile(pattern_str)

    matcger = regex.match(log_line)
    info ={k:ops.get(k,lambda x:x)(v) for k,v in matcger.groupdict().items()}
    print(info)


extract(log_line)