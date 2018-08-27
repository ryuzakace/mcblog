from flask import Flask
from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wubba lubba dub dub'
app.config.from_object(Config)

from app import routes
