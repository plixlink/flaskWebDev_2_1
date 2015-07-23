__author__ = 'user'

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s !<h1>' % name

@app.route('/UA')
def index_ua():
    user_agent = request.headers.get('User-Agent')
    return '<p>Yor browser is %s</p>' % user_agent

@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirect')
def redirect():
    return redirect('http://www.google.com')

@app.route('/admin/<id>')
def admin(id):
    admin = load_user(id)
    if not admin:
        abort(404)
    return ('<p>Hello, %s!</p>') % admin.name

if __name__ == '__main__':
    app.run(debug=True)
