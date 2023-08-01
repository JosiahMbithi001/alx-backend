#!/usr/bin/env python3
"""This File Mocks A Login"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Configuration
class Config:
	"""This Class Configures Babel"""
    LANGUAGES = ['en', 'fr', 'kg']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

# Function to get the user dictionary based on user ID
def get_user(user_id):
	"""This File Returns Get User"""

    return users.get(user_id)

# Before request function to set the global g.user based on login_as parameter
@app.before_request
def before_request():
    """This Function happens Before Request"""

	g.user = None
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))

# Locale selector function for Babel to determine the user's preferred language
@babel.localeselector
def get_locale():
    """ If the user is logged in and has a valid locale, use it"""
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    
    # Otherwise, fall back to the default behavior based on browser preferences
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Route to render the template
@app.route('/')
def index():
	""" This Returns Home"""

    return render_template('5-index.html')
    
if __name__ == '__main__':
    app.run()
