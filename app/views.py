
from flask import render_template, redirect, url_for
from app import app, db
from .models import User
import json

@app.route('/')
def index():
    return render_template('show_form.html',
                           title='Vue Request')

@app.route('/api/name', methods=['GET'])
def get_name():
    users = User.query.all()
    names = []
    for user in users:
        names.append(user.name)
    return json.dumps(names)

@app.route('/api/name/<name>', methods=['POST'])
def post_name(name):
    u = User(name=name)
    db.session.add(u)
    db.session.commit()
    return redirect(url_for('index'))
