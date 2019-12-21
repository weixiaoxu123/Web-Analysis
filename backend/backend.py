from flask import Flask,request
from flask import render_template
from sklearn.externals import joblib
import sys
sys.path.append('..')
import json
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import logging


app = Flask(__name__)
#  爬虫模块
datas = np.array(['URL','zimu_num','shuzi','zifu_num','url_T_num', 'inner','out','sum','bili','req_type_num','hanjian_host_num','iframe_num','eval_num','location_num','setTimeout_num','setInterval_num','scriptObjectsrc_num','scriptObjectsetAttribute_num','scriptObjectinnerHTML_num','windowopen_num'])
def readHTML(link):
    url=link
    req = requests.get(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
            })
    #按格式读取网页
    req.HTML = BeautifulSoup(req.text.encode('utf-8'),"html.parser")
    return req.HTML

def featrue_code(url):
    try:
        data=readHTML(url)
        iframe_num=str(data).count('iframe')           
        eval_num=str(data).count('eval')
        location_num=str(data).count('location')
        setTimeout_num=str(data).count('setTimeout')
        setInterval_num=str(data).count('setInterval')
        scriptObjectsrc_num=str(data).count('scriptObject.src')
        scriptObjectsetAttribute_num=str(data).count('scriptObject.setAttribute')
        scriptObjectinnerHTML_num=str(data).count('scriptObject.innerHTML')
        windowopen_num=str(data).count('window.location')
    except:
        iframe_num = -1          
        eval_num = -1
        location_num = -1
        setTimeout_num=-1
        setInterval_num=-1
        scriptObjectsrc_num=-1
        scriptObjectsetAttribute_num=-1
        scriptObjectinnerHTML_num=-1
        windowopen_num=-1
    data_code=np.array([int(iframe_num),int(eval_num),int(location_num),int(setTimeout_num),int(setInterval_num),int(scriptObjectsrc_num),int(scriptObjectsetAttribute_num),int(scriptObjectinnerHTML_num),int(windowopen_num)])
    return data_code 


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
    
    #空值处理
    for i in range(6):
        if neiwai[i]:
            neiwai[i]=neiwai[i]
        else:
            neiwai[i]=0

    f_code=list(np.array(featrue_code(url)))
    data=np.array([int(zimu_num),int(shuzi_num),int(zifu_num),int(T_zifu_num)] +neiwai+f_code)
    #global datas
    #datas = np.vstack((datas,data))
    #datass=pd.DataFrame(datas)
   
    RF_model=joblib.load('RF_model.m')
    logger.info("=============================================")
    logger.info(url+"的特征如下：")
    #logger.info(datas)
    logger.info(data)

    predicted = RF_model.predict(data.reshape(1,-1))
    logger.info("================predicted====================")
    logger.info(url + '的预测结果是:')
    logger.info(predicted)
    logger.info("==================over=======================")
    logger.info("=============================================")

    # data = pd.DataFrame(data,columns={'zimu_num','shuzi','zifu_num','url_T_num', 'inner','out','sum','bili','req_type_num','hanjian_host_num'})
    if predicted==0:
        return json.dumps({"res":0})
    else:
        return json.dumps({"res":1})
    


    
if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    
    handler = logging.FileHandler('./web-detection.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    handler.setFormatter(logging_format)
    logger.addHandler(handler)
   
    logger.info('============= 恶意网页系统检测已启动=============')
    app.run(port=2222,debug=True)