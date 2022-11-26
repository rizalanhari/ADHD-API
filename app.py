from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

url = "https://raw.githubusercontent.com/rizalanhari/ADHD-API/main/DataTrainApi.csv"
dataTrain = pd.read_csv(url)

@app.route('/')
def getHello():
    return "Hello, API ADHD"

@app.route('/datatrain')
def getDataTrain():
    return dataTrain.to_json(orient='records')

if __name__ == '__main__':
    app.run()