
from flask import render_template
from app import app, db
from .models import User

@app.route('/')
def index():
    return render_template('show_form.html')

@app.route('/api/name', methods=['GET'])
def get_name():
    users = User.query.all()

@app.route('/api/name/', methods=['POST'])
def post_name():
    User(name=name)