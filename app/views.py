
from flask import render_template, redirect, url_for, g, request
from flask_httpauth import HTTPTokenAuth
from app import app, db
from .models import User
import json

from flask_cors import cross_origin

auth = HTTPTokenAuth(scheme='Token')

tokens = {
    'secret-token-1': 'John',
    'secret-token-2': 'Susan'
}

@auth.verify_token
def verify_token(token):
    print token
    if token in tokens:
        g.current_user = tokens[token]
        return True
    return False

@app.route('/')
@cross_origin()
@auth.login_required
def index():
    # print request.headers
    # print 'Hello %s!' % g.current_user
    return None

@app.route('/api/name', methods=['GET'])
@cross_origin()
@auth.login_required
def get_name():
    # print 'here'
    users = User.query.all()
    names = []
    for user in users:
        names.append(user.name)
    print names
    return json.dumps(names)

@app.route('/api/name/<name>', methods=['POST'])
def post_name(name):
    u = User(name=name)
    db.session.add(u)
    db.session.commit()
    return redirect(url_for('index'))
