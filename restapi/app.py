from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<p> Welcome Home</p>'

@app.route('/<name>')
def print_name(name):
    return f'Call me: {name}'