import flask
from flask import Flask, request, jsonify
import numpy as np
import pickle
import requests

app = Flask(__name__)


# 메인 페이지 라우팅
@app.route("/")
def index():
    return "<h1>hello</h1>"


# 데이터 예측 처리
@app.route('/predict', methods=['GET'])
def make_prediction():
    if request.method == 'GET':

        # 입력 받은 값 예측
        prediction = model.predict([[15,40,1000,25]]) # 1이 출력되어야함
        output = prediction[0]
        # 결과 리턴
        return str(output)


if __name__ == '__main__':
    # 모델 로드
    # ml/model.py 선 실행 후 생성
    model = pickle.load(open('./model/test.pkl','rb'))
    # Flask 서비스 스타트
    app.run(host='0.0.0.0', port=5000, debug=True)
