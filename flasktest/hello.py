from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return f'<h1>Hello, {escape(name)}!</h1>'

