#!/usr/bin/env python3
"""This Forces Locale in The URL Parameters"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Configuration
class Config:
	"""This Class Configures Babbel"""
	LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():

    """ Check if the locale parameter is present in the request args"""
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    # If the locale parameter is not present or not supported, use the previous default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
	"""Render Home Page"""

    return render_template('4-index.html')

if __name__ == '__main__':
    app.run()
