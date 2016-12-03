
from flask import render_template, jsonify
from app import app, db
from .models import User
import json

@app.route('/')
def index():
    return render_template('show_form.html')

@app.route('/api/name', methods=['GET'])
def get_name():
    users = User.query.all()
    names = []
    for user in users:
        names.append(user.name)
    return json.dumps(names)

@app.route('/api/name/', methods=['POST'])
def post_name():
    u = User(name=name)
    db.session.add(u)
    db.session.commit()
