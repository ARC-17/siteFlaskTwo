from flask import Flask
from src.routes import routes

app = Flask(__name__)

app.add_url_rule(routes["test_route"],view_func=routes[""])
