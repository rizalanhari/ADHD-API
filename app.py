from flask import Flask, jsonify, request
import pandas as pd

dataTrain = pd.read_csv("dataTrainAPI.csv")

app = Flask(__name__)

@app.route('/')
def getHello():
    return "Hello, API ADHD"

@app.route('/datatrain')
def getDataTrain():
    return dataTrain.to_json(orient='records')

if __name__ == '__main__':
    app.run()