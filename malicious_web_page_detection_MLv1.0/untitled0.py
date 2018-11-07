# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 13:20:21 2018

@author: eweixux
"""
import pandas as pd
import numpy as np


neiwai=[1,2,3,None]

a = np.array(neiwai)
for i in range(4):
    if neiwai[i]:
        neiwai[i]=neiwai[i]
    else:
        neiwai[i]=0
        

print(neiwai)
    
    
