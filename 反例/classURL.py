# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:29:51 2018

@author: wx
"""

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import re

"""
read webpage html and js file..
"""
def readHTML(link):
    url=link
    req = requests.get(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            })
    
    #按格式读取网页
#    req.HTML = BeautifulSoup(req.text.encode('utf-8'),"html.parser")
#    return req.HTML
    #open网页
    return req
#写入文件
#    writer = pd.ExcelWriter('output.xlsx')
#    df.to_excel(writer,'Sheet1')
#    writer.save()  

    

      
if __name__=='__main__':

    """
    获取via 数据
    """
    i=0
    trojan=[]
    direct=[]
    url_lizi = pd.read_csv('export.csv',encoding='ISO-8859-1',names=['date','url','ip','ip2','type','loading','3eee3','guojia'])
#    url_link = url_lizi['url']
    
#    all url's type list 
    url_type = url_lizi['ip']
    for i in range(len(url_type)):
        if(url_type[i].find('rojan')==1):
            url_type[i] = "Trojan"
        elif(url_type[i].find('edirect')==1):
            url_type[i] = "redirect"
        else:
            url_type[i] = "other"
        
            
    url_type_list=[]
    for type in url_type:
        if type not in url_type_list:
            url_type_list.append(type)
    print(url_type_list)
#    
#    # type = Trojan    URL
#    alexa_muma = url_lizi[url_lizi['ip']=='Trojan']
#    for link in url_link:
#        i=i+1
#        try:
#            data=readHTML(link)
#            print(str(i)+":"+ data.headers['link'])
#        except:
#            print(str(i)+":error!")
                 
    
