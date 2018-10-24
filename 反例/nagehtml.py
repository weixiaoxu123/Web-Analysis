# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:05:00 2018

@author: eweixux
"""

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import re



"""
 获取url 的特征 特殊字符个数zifu_num，数字个数shuzi_num，字母个数zimu_num。。

"""
def feature_Url():
    url_len=[]
    url_zifu_num=[]
    url_shuzi_num=[]
    url_zimu_num=[]
    positive = pd.read_csv('./phishtank/nagetive.csv')
    positive_url = positive['link']
   
    for link in positive_url:
        zifu_num=0
        shuzi_num=0
        zimu_num=0
        url_len.append(len(link))
        for str in link:
            if str.isalpha():
                zimu_num+=1
            elif str.isdigit():
                shuzi_num+=1
            else:
                zifu_num+=1
        url_zimu_num.append(zimu_num)   
        url_shuzi_num.append(shuzi_num) 
        url_zifu_num.append(zifu_num)  
    positive.insert(2,'zimu_num',url_zimu_num)
    positive.insert(3,'shuzi',url_shuzi_num)
    positive.insert(4,'zifu_num',url_zifu_num)
    
    positive.to_csv('nage_url.csv',index=False)
    return positive



"""
read webpage html and js file..
"""
def readHTML(link):
    url=link
    print("正在读取："+url)
    req = requests.get(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            })
    #按格式读取网页
    req.HTML = BeautifulSoup(req.text.encode('utf-8'),"html.parser")
    return req.HTML

def featrue_code(positive_url):
    code_iframe_num=[]
    code_eval_num=[]
    code_location_num=[]
    for link in positive_url:
        iframe_num=0
        location_num=0
        eval_num=0
        try:
            data=readHTML(link)
            iframe_num=str(data).count('iframe')           
            eval_num=str(data).count('eval')
            location_num=str(data).count('location')
            print(link)
            print(iframe_num)
            print(location_num)
            print(eval_num)
        except:
            iframe_num = -1          
            eval_num = -1
            location_num = -1
            print(link)
            print(iframe_num)
            print(location_num)
            print(eval_num)
        code_iframe_num.append(iframe_num)
        code_eval_num.append(eval_num)
        code_location_num.append(location_num)
        
    positive.insert(5,'iframe_num',code_iframe_num)
    positive.insert(6,'location_num',code_location_num)
    positive.insert(7,'eval_num',code_eval_num)
    
    positive.to_csv('nage_url_code.csv',index=False)
    return positive

if __name__=='__main__':
    link='http://www.iamagameaddict.com/'
    data = readHTML(link)
    #  add url fearture
<<<<<<< HEAD
#    positive = pd.read_csv('nage_url.csv')
#    positive_url = positive['link']
##    positive = feature_Url()
=======
#    positive = pd.read_csv('nage_url——code.csv')
#    positive_url = positive['link']
#    positive = feature_Url()
    nage_url_code=pd.read_csv('nage_url_code.csv')
>>>>>>> b88175939b8e5f4a5ca596f9d73a228347d8c7dc
#    positive = featrue_code(positive_url)

