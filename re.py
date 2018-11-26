# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:49:33 2018

@author: wx
"""
import re
import shutil,os


uplist = ['CXP123456_1-R1A232','CXP123456_1-R1A252','CXP123456_1-R1A242','CXP123456_1-R1A222','CXP123456_1-R1A262','CXP123456_1-R1A262aaa','CXP123456_1-a1A262','CXP123456_1-R1A262A111']

pattren=r'[A-Za-z0-9]*_[A-Za-z0-9]-R[0-9]*[A-Za-z]*[0-9]*$'
abc = []
for up in uplist:
    res = re.match(pattren,up)
    if res:
        abc.append(res.group())

abc = sorted(abc,reverse=True)

print(abc)

abc[1]


#shutil.copy(path1,path2)


if 'CXP123456_1-R1A232e3242342' in uplist:
    print("ok")
else:
    print("no")

