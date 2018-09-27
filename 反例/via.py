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
#    i=0
#    html_error=[]
#    html_code=[]
#    alexa_lizi = pd.read_csv('alexaScraping.csv')
#    alexa_link = alexa_lizi['link']
#    
#    for link in alexa_link:
#        i=i+1
#        print("loading........."+ str(i/500) +"%")
#        try:
#            html_code.append(readHTML(link))
#        except:
#            print(link)
#                 
#    print("----ok----")
#    print(html_code[6])   
#    data=readHTML("https://toddscarwash.com/")
#    print(re.findall(r'(?<=src=\").*?(?=\")|(?<=src=\').*?(?=\')|(?<=href=\").*?(?=\")|(?<=href=\').*?(?=\')',str(BeautifulSoup(data.text.encode('utf-8'),"html.parser"))))
#    urllist=re.findall(r'(?<=src=\").*?(?=\")|(?<=src=\').*?(?=\')|(?<=href=\").*?(?=\")|(?<=href=\').*?(?=\')',str(BeautifulSoup(data.text.encode('utf-8'),"html.parser")))
#    for url in urllist:
#        print(url)
        
#    writer = pd.ExcelWriter('output.xlsx')
#    df.to_excel(writer,'Sheet1')
#    writer.save()  

    """
    获取via 数据
    """
    i=0
    via_error=[]
    via_true=[]
    alexa_lizi = pd.read_csv('export.csv',encoding='ISO-8859-1',names=['date','url','ip','ip2','type','loading','3eee3','guojia'])
    alexa_link = alexa_lizi['url']
    
   # all url's type list 
    alexa_type = alexa_lizi['ip']
    alexa_type_lisrt=[]
    for type in alexa_type:
        if type not in alexa_type_lisrt:
            alexa_type_lisrt.append(type)
    print(alexa_type_lisrt)
    
    # type = Trojan    URL
    alexa_muma = alexa_lizi[alexa_lizi['ip']=='Trojan']
    for link in alexa_link:
        i=i+1
        try:
            data=readHTML(link)
            print(str(i)+":"+ data.headers['link'])
        except:
            print(str(i)+":error!")
                 
    print("----ok----")
    
