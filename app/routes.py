from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Shirish'}
    
    posts = [
        {
            'author': {'username': 'Mark Manson'},
            'body': 'Avoid Entitlement!'
        },
        {
            'author': {'username': 'Amish Tripathi'},
            'body': 'The Universe bows to lord Shiva, I bow to lord Shiva!'
        }
    ]

    return render_template('index.html', title = 'Home', user = user, posts = posts)
