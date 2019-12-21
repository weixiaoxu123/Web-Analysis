import requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np


datas = np.array(['url','iframe_num','eval_num','location_num','setTimeout_num','setInterval_num','scriptObjectsrc_num','scriptObjectsetAttribute_num','scriptObjectinnerHTML_num','windowopen_num'])                                                                                      

def readHTML(link):
    url=link
    print("正在读取："+url)
    req = requests.get(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            })
    #按格式读取网页
    req.HTML = BeautifulSoup(req.text.encode('utf-8'),"html.parser")
    return req.HTML

def featrue_code(url):
    try:
        data=readHTML(url)
        iframe_num=str(data).count('iframe')           
        eval_num=str(data).count('eval')
        location_num=str(data).count('location')
        setTimeout_num=str(data).count('setTimeout')
        setInterval_num=str(data).count('setInterval')
        scriptObjectsrc_num=str(data).count('scriptObject.src')
        scriptObjectsetAttribute_num=str(data).count('scriptObject.setAttribute')
        scriptObjectinnerHTML_num=str(data).count('scriptObject.innerHTML')
        windowopen_num=str(data).count('window.location')
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
    data=np.array([int(iframe_num),int(eval_num),int(location_num),int(setTimeout_num),int(setInterval_num),int(scriptObjectsrc_num),int(scriptObjectsetAttribute_num),int(scriptObjectinnerHTML_num),int(windowopen_num)])
    print(data) 
    

if __name__=='__main__':
    featrue_code('http://www.baidu.com')
