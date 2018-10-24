# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:55:45 2018

@author: eweixux
"""

#import requests
import webbrowser as web
import pandas as pd

if __name__ =='__main__':
#    allUrl = pd.read_csv('alexaScraping.csv')
#    urlLink = allUrl['link']
    urlLink=['www.baidu.com']
    
    for link in urlLink:
        web.open(link,1)
        
      