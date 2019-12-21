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


def entropy(data,ind):
    '''
    :param data: 数据集
    :param att_name: 属性名
    :return: entropy
    '''
    levels = data[ind].unique()
    ent = 0
    for lv in levels:
        pi = sum(data[ind]==lv) / data.shape[0]
        ent += pi * np.log2(pi)

    return -ent


print('\n 好网页的信息的信息熵：', entropy(data, 19))


def conditional_entropy(data, xind, yind):
    xs = data[xind].unique()
    ys = data[yind].unique()
    p_x = data[xind].value_counts() / data.shape[0]
    ce = 0
    fu=0
    for x in xs:
        ce += p_x[x] * entropy(data[data[xind]==x], yind)
#    for x in xs:
#        fu += (1-p_x[x]) * entropy(data[data[xind]!=x],yind)
#        
    return ce+fu

def zengyilv(data,ind):
    levels = data[ind].unique()
    res=0
    for i in levels:
        pi = len(levels) / data.shape[0]
        res += pi * np.log2(pi)
    return -res


print('\n V0条件下，好的信息熵：', conditional_entropy(data, 0, 19))


def gain(data, xind, yind):
    ent = entropy(data, yind)
    ce = conditional_entropy(data, xind, yind)
    return (ent - ce)/zengyilv(data,xind)

#def gain(data, xind, yind):
#    ent = entropy(data, yind)
#    ce = conditional_entropy(data, xind, yind)
#    return ent - ce

print('\n V0条件下，好的信息增益：', gain(data, 0, 19))

gain_list = []
print('\n全部特征的信息增益：')
for name in data.columns[:-1]:
    name_gain = gain(data, name, 19)
    gain_list.append(name_gain)
    print('V'+str(name), name_gain)


#def gini_index(data, xind, yind):
#    xs = data[xind].unique()
#    p_x = data[xind].value_counts() / data.shape[0]
#
#    gi_index = 0
#
#    for x in xs:
#        data_x = data[data[xind]==x]
#        ys = data[yind].unique()
#        gi = 1
#
#        for y in ys:
#            if y not in data_x[yind].value_counts():
#                continue
#
#            gi -= np.square(data_x[yind].value_counts()[y] / data_x.shape[0])
#
#        gi_index += p_x[x] * gi
#
#    return gi_index


#print(gini_index(data, 0, 19))

#gini_list = []
#print('\n全部的基尼指数：')
#for name in data.columns[:-1]:
#    name_gi = gini_index(data, name, 19)
#    gini_list.append(name_gi)
#    print(name, name_gi)

x = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']
plt.plot(x, gain_list)
#plt.plot(x, gini_list)
plt.show()
    