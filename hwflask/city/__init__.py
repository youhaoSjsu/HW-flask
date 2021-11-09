from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# instance of the Flask class
app = Flask(__name__)
app.config.from_mapping(
            SECRET_KEY = 'it-dont-matter'
            )

from city import routes
