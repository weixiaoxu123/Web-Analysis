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
def feature_Url(urlList):
    url_len=[]
    url_zifu_num=[]
    url_shuzi_num=[]
    url_zimu_num=[]
    positive = pd.read_csv('positive.csv')
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
    
    positive.to_csv('posi_url.csv',index=False)
    return positive



"""
read webpage html and js file..
"""
def readHTML(link):
    url=link
    req = requests.get(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            })
    #按格式读取网页
    req.HTML = BeautifulSoup(req.text.encode('utf-8'),"html.parser")
    return req.HTML
    #open网页
#    return req

      
if __name__=='__main__':
    #  add url fearture
    positive = pd.read_csv('posi_url.csv')
    positive_url = positive['link']
#    positive = feature_Url(positive_url)
    
   #http fearture
   
   # html  js  fearture
#    for link in positive_url:
#        html = readHTML(link)
#        
        
        

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
 

                 

    
