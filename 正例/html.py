# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:05:00 2018

@author: eweixux
"""
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np
import re

# 获取代码和url的特征，，，，

"""
 获取url 的特征 特殊字符个数zifu_num，数字个数shuzi_num，字母个数zimu_num。。

"""

datas =np.array(['url','iframe_num','eval_num','location_num','setTimeout_num','setInterval_num','scriptObjectsrc_num','scriptObjectsetAttribute_num','scriptObjectinnerHTML_num','windowopen_num'])                                                                                      
def feature_Url():
    url_len=[]
    url_zifu_num=[]
    url_shuzi_num=[]
    url_zimu_num=[]
    url_T_zifu_num=[]
    positive = pd.read_csv('alexa6.4-1000-2000.csv')
    positive_url = positive['link']
   
    for link in positive_url:
        
        zifu_num=0
        shuzi_num=0
        zimu_num=0
        T_zifu_num=0
        url_len.append(len(link))
        for str in link:
            if str.isalpha():
                zimu_num+=1
            elif str.isdigit():
                shuzi_num+=1
            else:
                zifu_num+=1
        T_zifu_num =zifu_num - ( link.count('.') + link.count(':') + link.count('/'))
        url_zimu_num.append(zimu_num)   
        url_shuzi_num.append(shuzi_num) 
        url_zifu_num.append(zifu_num)
        url_T_zifu_num.append(T_zifu_num)
    
    positive.insert(2,'zimu_num',url_zimu_num)
    positive.insert(3,'shuzi',url_shuzi_num)
    positive.insert(4,'zifu_num',url_zifu_num)
    positive.insert(5,'url_T_zifu_num',url_T_zifu_num)
    
    positive.to_csv('6.4-positive-1000-2000.csv',index=False)
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
#    code_iframe_num=[]
#    code_eval_num=[]
#    code_location_num=[]
#    code_setTimeout_num=[]
#    code_setInterval_num=[]
#    code_scriptObjectsrc_num=[]
#    code_scriptObjectsetAttribute_num=[]
#    code_scriptObjectinnerHTML_num=[]
##    code_iframeObjectsrc_num=[]
##    code_iframeObjectsetAttribute_num=[]
#    code_windowopen_num=[]
    
    for i in range(3800,len(positive_url)):
        iframe_num=0
        location_num=0
        eval_num=0
        setTimeout_num=0
        setInterval_num=0
        scriptObjectsrc_num=0
        scriptObjectsetAttribute_num=0
        scriptObjectinnerHTML_num=0
        windowopen_num=0
        try:
            data=readHTML(positive_url[i])
            iframe_num=str(data).count('iframe')           
            eval_num=str(data).count('eval')
            location_num=str(data).count('location')
            setTimeout_num=str(data).count('setTimeout')
            setInterval_num=str(data).count('setInterval')
            scriptObjectsrc_num=str(data).count('scriptObject.src')
            scriptObjectsetAttribute_num=str(data).count('scriptObject.setAttribute')
            scriptObjectinnerHTML_num=str(data).count('scriptObject.innerHTML')
            windowopen_num=str(data).count('window.location')
            print(str(i)+'==='+positive_url[i])
        except:
            iframe_num = -1          
            eval_num = -1
            location_num = -1
            setTimeout_num=-1
            setInterval_num=-1
            scriptObjectsrc_num=-1
            scriptObjectsetAttribute_num=-1
            scriptObjectinnerHTML_num=-1
            windowopen_num=-1
        global datas
        data=np.array([positive_url[i],int(iframe_num),int(eval_num),int(location_num),int(setTimeout_num),int(setInterval_num),int(scriptObjectsrc_num),int(scriptObjectsetAttribute_num),int(scriptObjectinnerHTML_num),int(windowopen_num)])
        datas = np.vstack((datas,data))
        datass=pd.DataFrame(datas)
        print(data)  
        datass.to_csv('6-4/nage_html_5000.csv',header=0,index=0)
        
#        code_iframe_num.append(iframe_num)
#        code_eval_num.append(eval_num)
#        code_location_num.append(location_num)
#        code_setTimeout_num.append(setTimeout_num)
#        code_setInterval_num.append(setInterval_num)
#        code_scriptObjectsrc_num.append(scriptObjectsrc_num)
#        code_scriptObjectsetAttribute_num.append(scriptObjectsetAttribute_num)
#        code_scriptObjectinnerHTML_num.append(scriptObjectinnerHTML_num)
#        code_windowopen_num.append(windowopen_num)
#    positive.insert(11,'iframe_num',code_iframe_num)
#    positive.insert(12,'location_num',code_location_num)
#    positive.insert(13,'eval_num',code_eval_num)
#    positive.insert(14,'setTimeout_num',code_setTimeout_num)
#    positive.insert(15,'setInterval_num',code_setInterval_num)
#    positive.insert(16,'scriptObjectsrc_num',code_scriptObjectsrc_num)
#    positive.insert(17,'scriptObjectsetAttribute_num',code_scriptObjectsetAttribute_num)
#    positive.insert(18,'scriptObjectinnerHTML_num',code_scriptObjectinnerHTML_num)
#    positive.insert(19,'windowopen_num',code_windowopen_num)
    
  #  positive.to_csv('positive_allfeatures6.4.csv',index=False)
    return positive

if __name__=='__main__':
    #  add url fearture
#    positive = pd.read_excel('nage.xlsx')
#    positive = pd.read_csv('nage-5000.csv')
#    positive_url = positive['link']
#    positive = feature_Url()
#    positive = featrue_code(positive_url)
    data=readHTML('http://www.baidu.com')
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
 

                 

    
