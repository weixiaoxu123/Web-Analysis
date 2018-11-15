# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:09:29 2018

@author: wx
"""
import requests
from bs4 import BeautifulSoup
import re

def readHTML(link):
    url=link
    print("正在读取："+url)
    req = requests.get(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            })
    #按格式读取网页
    req.HTML = BeautifulSoup(req.text.encode('utf-8'),"html.parser")
    return req.HTML

if __name__=='__main__':
    url = 'http://www.zynga.com'
    data = readHTML(url)
    print(data)
    print(str(data).count('.exe'))
    print(re.findall(r'/.*\.exe',str(data)))