from flask import Flask
#=nb
app = Flask(__name__)
@app.route('/')
def hello():
    return "hello world"