from sklearn.externals import joblib
import numpy as np


def main():
    url = 'http://www.baidu.com'
    neiwai=[7,24,31,0.22580]
    zifu_num=0
    shuzi_num=0
    zimu_num=0
    T_zifu_num=0
    for str in url:
        if str.isalpha():
            zimu_num+=1
        elif str.isdigit():
            shuzi_num+=1
        else:
            zifu_num+=1
    T_zifu_num =zifu_num - ( url.count('.') + url.count(':') + url.count('/'))
    svm_model=joblib.load('svm.m')
    data=np.array([zimu_num,shuzi_num,zifu_num,T_zifu_num] + neiwai)
    predicted = svm_model.predict(data.reshape(1,-1))
    print(predicted)
    
if __name__=='__main__':
    main()