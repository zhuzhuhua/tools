# -*- coding: UTF-8 -*-
import urllib2

def download1(url):
    return urllib2.urlopen(url).read() #读取全部网页


def download2(url):
    return urllib2.urlopen(url).readlines() #读取每一行的网页数据，压入到列表


def download3(url):
    response = urllib2.urlopen(url)
    while True:
        line = response.readline()
        print line
        if not line:
            break

if __name__ == '__main__':
    print download1("https://www.baidu.com")