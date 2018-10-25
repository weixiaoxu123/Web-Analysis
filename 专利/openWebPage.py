# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:55:45 2018

@author: eweixux
"""

#import requests

import pandas as pd
import numpy as np

if __name__ =='__main__':
    data2=pd.DataFrame(columns=['URL','inner','out','sum','bili'])
    f = open('nozheng.txt')   
    data=f.read().split()
    for da in data:
        da = [da.split(',')]
        dda = pd.DataFrame(da,columns=['URL','inner','out','sum','bili'])
        print(dda)
        data2 = data2.append(dda,ignore_index = True)
        
    print(data2)
    data2.to_csv('nagetive_ZL2.csv',index=False)
#        data2.append(da)
    
#    (data)
#    data2 = pd.DataFrame(data)
    