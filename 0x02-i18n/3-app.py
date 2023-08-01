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

@babel.localeselector
def get_locale():
    """ Check if the user has explicitly set the language using URL parameter"""
    if 'lang' in request.args:
        return request.args.get('lang')

    # Check the supported languages from request.accept_languages
    supported_languages = app.config['LANGUAGES']
    return request.accept_languages.best_match(supported_languages)

