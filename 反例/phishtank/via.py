# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 16:47:33 2018

@author: wx
"""

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

      
if __name__=='__main__':
    """
    获取via 数据
    """
    i=0
    via_error=[]
    via_true=[]
    alexa_lizi = pd.read_csv('verified_online.csv',encoding='ISO-8859-1')
    alexa_link = alexa_lizi['url']
    
    for link in alexa_link:
        i=i+1
        try:
            data=readHTML(link)
            via_true.append(link)
            print(link)
        except:
            via_error.append(link)
            print(i)
                 
    print("----ok----")
    
