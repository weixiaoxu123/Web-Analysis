# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:05:00 2018

@author: eweixux
"""

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


def readHTML(link):
    url=link
    req = requests.get(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            })
    req.HTML = BeautifulSoup(req.text.encode('utf-8'),"html.parser")
    return req.HTML
      
if __name__=='__main__':
    i=0
    html_error=[]
    html_code=[]
    alexa_lizi = pd.read_csv('alexaScraping.csv')
    alexa_link = alexa_lizi['link']
    
    for link in alexa_link:
        i=i+1
        print("loading........."+ str(i/500) +"%")
        try:
            html_code.append(readHTML(link))
        except:
            print(link)
                 
    print("----ok----")
    print(html_code[6])   
    
        
      
     
        
        
        
#    writer = pd.ExcelWriter('output.xlsx')
#    df.to_excel(writer,'Sheet1')
#    writer.save()  


