# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:51:35 2018

@author: eweixux
"""

import requests
from bs4 import BeautifulSoup


def excuteSpider(url,headers,session,):
    req = session.get(url, headers=headers)
    bsObj = BeautifulSoup(req.text, 'html.parser')

    rankList = bsObj.findAll("div", {"class": "rank-index"})
    linkList = bsObj.findAll("span", {"class": "domain-link"})
    nameList = bsObj.findAll("div", {"class": "infos"})
    lranksub=[]
    llinksub=[]
    lnamesub=[]             
    
    
    for rank in rankList:

        # print rank.string
        lranksub.append(rank.string.encode('utf-8').decode())

    # print lrank

    for link in linkList:
        llinksub.append(link.a['href'].encode('utf-8').decode())
        # print link.a['href']
    # print llink

    for name in nameList:
        str1 = name.contents[0].encode('utf-8').decode()
        s=str1.split('（')
        lnamesub.append(s[0])
        # print (s[0])
    return lranksub,llinksub,lnamesub


if __name__=='__main__':
    print("begain=========")
    lrank=[]
    llink=[]
    lname=[]

    session = requests.Session()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
           "Accept": "*/*"}
    for i in range(51,100):
        print('page'+str(i))
        if i==1:
            url = "http://www.alexa.cn/siterank/" 
        else:
            url = "http://www.alexa.cn/siterank/"+str(i)   

        lranksub,llinksub,lnamesub=excuteSpider(url, headers, session)
        lrank+=lranksub
        llink+=llinksub
        lname+=lnamesub
    print("writing to csv........")
    wf = open('./alexa6.4-1000-2000.csv', 'w')
    wf.write('rank,link,name\n')
    for i in range(len(lrank)):
        wf.write('%s,%s,%s\n' %(lrank[i],llink[i],lname[i]))
    wf.close()
    print('ok')
    