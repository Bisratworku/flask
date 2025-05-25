from flask import Flask
from markupsafe import escape
#=nb
app = Flask(__name__)

@app.route('/')
def index():
    return f'well come to my website'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/<name>')
def coustom(name):
    return f'Hello {escape(name)}'

@app.route('/about/<username>')
def show_user_profile(username):
    return f'User {escape(username)} information page'

@app.route('/path')
def show_path():
    return 'This is a path page'
@app.route('/path/<path:subpath>')#the comverter accepts a path, string, int, float and uuid
def show_subpath(subpath):
    return f'This is a subpath: {escape(subpath)}'