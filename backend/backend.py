from flask import Flask,request
from flask import render_template
import json

app = Flask(__name__)


@app.route('/')
def start():
    return render_template('index.html')

    
@app.route('/test',methods=['POST'])
def test():
    a = request.json['name']
    print(a)
    return json.dumps({"res":"ok"})


if __name__ == '__main__':
    app.run(port=2222,debug=True)