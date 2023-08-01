#!/usr/bin/env python3
"""This File Instantiates babel"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)

# Instantiate the Babel object
babel = Babel(app)


class Config:
	"""This Class Configures Languages, Default Language and Timezone"""
	LANGUAGES = ["en", "fr"]
	BABEL_DEFAULT_LOCALE = "en"
	BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

