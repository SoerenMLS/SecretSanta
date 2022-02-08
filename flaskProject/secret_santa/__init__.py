from flask import Flask
from flask_cors import CORS
from configuration import Config

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
CORS(app)

from secret_santa import routes
