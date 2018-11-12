from flask import Flask,request
from flask import render_template
from sklearn.externals import joblib
import json
import numpy as np
import pandas as pd

app = Flask(__name__)

datas = np.array(['URL','zimu_num','shuzi','zifu_num','url_T_num', 'inner','out','sum','bili','req_type_num','hanjian_host_num'])

@app.route('/')
def start():
    return render_template('index.html')

    
@app.route('/test',methods=['POST'])
def test():
    # data = request.json['data']
    # print(data)
    # return json.dumps({"res":0})

    url = request.json['url']
    neiwai=request.json['neiwai']
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
    # svm_model=joblib.load('LR_model.m')
    #空值处理
    # a = np.array(neiwai)
    for i in range(6):
        if neiwai[i]:
            neiwai[i]=neiwai[i]
        else:
            neiwai[i]=0
    
    global datas
    data=np.array([url,int(zimu_num),int(shuzi_num),int(zifu_num),int(T_zifu_num)] + neiwai)
    datas = np.vstack((datas,data))
    datass=pd.DataFrame(datas)
    print(data)
    
    datass.to_csv('positive_hanjia.csv',header=0,index=0)
    # print('\n')
    # print("=================================================================")
    # print("================"+url+"=========================")
    # print(data)
    # predicted = svm_model.predict(data.reshape(1,-1))
    # print("================="+"predicted"+"===========================")
    # print(predicted)
    # print("======================="+"over"+"===========================")
    # print("==========================================================")


    # data = pd.DataFrame(data,columns={'zimu_num','shuzi','zifu_num','url_T_num', 'inner','out','sum','bili','req_type_num','hanjian_host_num'})
    # if predicted==0:
    #     return json.dumps({"res":0})
    # else:
    #     return json.dumps({"res":1})
    return json.dumps({"res":0})

if __name__ == '__main__':
    app.run(port=2222,debug=True)