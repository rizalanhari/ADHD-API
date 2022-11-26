from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def getHello():
    return "Hello, API ADHD"

if __name__ == '__main__':
    app.run()