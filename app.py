from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

dataTrain = pd.read_csv("https://raw.githubusercontent.com/rizalanhari/ADHD-API/main/DataTrainApi.csv")

@app.route('/')
def getHello():
    return "Hello, API ADHD"

@app.route('/datatrain')
def getDataTrain():
    return dataTrain.to_json(orient='records')

if __name__ == '__main__':
    app.run()