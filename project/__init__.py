from flask import Flask
import os

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = os.environ['FLASK_SECRET']

def create_app():
	with app.app_context():
		from . import routes
		return app
