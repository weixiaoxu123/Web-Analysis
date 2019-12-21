# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:12:24 2019

@author: wx
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 18:34:47 2019

@author: wx
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io

dataset= pd.read_excel('4.15test.xlsx',header=None)

data = dataset

print(data)


def entropy(data,ind,f = False):
    '''
    :param data: 数据集
    :param att_name: 属性名
    :return: entropy
    '''
    levels = data[ind].unique()
    ent = 0
    for lv in levels:
        flag = int(data[data[ind]==lv][ind].value_counts())/data.shape[0]
#        print(flag)
        pi = sum(data[ind]==lv) / data.shape[0]
        if f:
            ent += flag * pi * np.log2(pi)
        else:
            ent += pi * np.log2(pi)
    return -ent


print('\n 好网页的信息的信息熵：', entropy(data, 19))

#求取每个特征的信息增益
def conditional_entropy(data, xind, yind):
    xs = data[xind].unique()
    ys = data[yind].unique()
    p_x = data[xind].value_counts() / data.shape[0]
    ce = 0
    fu=0
    for x in xs:            
        #ce += p_x[x] * entropy(data[data[xind]==x], yind,True)
        fu += (1-p_x[x]) * entropy(data[data[xind]!=x],yind)
        #print(str(x)+'的信息增益' + str(entropy(data, 19) -(0.9*ce+0.1*fu)))       
    return ce + fu

#求取所有特征的信息增益 
def conditional_entropy2(data, xind, yind):
    xs = data[xind].unique()
    ys = data[yind].unique()
    p_x = data[xind].value_counts() / data.shape[0]
    ce = 0
    for x in xs:            
        ce += p_x[x] * entropy(data[data[xind]==x], yind)      
    return ce


def gain(data, xind, yind):
    ent = entropy(data, yind)
    ce = conditional_entropy(data, xind, yind)
    return ent - ce

print('\n V0条件下，好的信息增益：', gain(data, 0, 19))
#
gain_list = []
print('\n全部特征的信息增益：')
for name in data.columns[:-1]:
    name_gain = gain(data, name, 19)
    gain_list.append(name_gain)
    print('V'+str(name), name_gain)




x = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
plt.plot(x, gain_list)
#plt.plot(x, gini_list)
plt.show()