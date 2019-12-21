import numpy as np
import pandas as pd


def feature_Url():
    url_len=[]
    url_zifu_num=[]
    url_shuzi_num=[]
    url_zimu_num=[]
    url_T_zifu_num=[]
    positive=pd.read_csv('nage_all_features.csv')
    print(positive['url'])
    positive_url = positive['url']

    link11=[]
    for link in positive_url:
        link =  link.split('/')[0]+'//'+link.split('/')[2] 
        link11.append(link)
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
        
    positive = positive.drop(columns=['url','zimu_num', 'shuzi','zifu_num','url_T_zifu_num'])
    positive.insert(0,'url',link11)
    positive.insert(1,'zimu_num',url_zimu_num)
    positive.insert(2,'shuzi',url_shuzi_num)
    positive.insert(3,'zifu_num',url_zifu_num)
    positive.insert(4,'url_T_zifu_num',url_T_zifu_num)
#    
    positive.to_csv('nage_all.csv',index=False)
    return positive


#data = pd.read_csv('11.csv')

#url =data['url']
aa = feature_Url()
