# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:09:43 2018

@author: eweixux
"""
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import re

def readHTML(link):
    url=link
    print("正在读取："+url)
    req = requests.get(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            })
    #按格式读取网页
#    req.HTML = BeautifulSoup(req.text.encode('utf-8'),"html.parser")
    return req


if __name__=='__main__':
    
    url = 'https://blog.csdn.net/'
    req = readHTML(url)
    data = str(BeautifulSoup(req.text.encode('utf-8'),"html.parser"))
    print('src:' + str(data.count('src=') + data.count('src =')))
    print('href:'+ str(data.count('href')))
    print('跳转location:' + str(data.count('location')))
    print('iframe:' + str(data.count('iframe')))
    print('动态eval:'+str(data.count('eval')))
    print('setIimeut:'+str(data.count('setTimeout')))
    print('setInterval:'+str(data.count('setInterval')))
    print('脚本插入：'+ str(data.count('scriptObject')+ data.count('iframeObject')))