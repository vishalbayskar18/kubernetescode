from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Great Going Vishal Keep it up .... Hola Famila!!!'
