#!/usr/bin/env python3
"""second app"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import g, request


app = Flask(__name__)
# app.config.from_pyfile('babel.cfg')
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ config class"""
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


@app.before_request
def before_request():
    """ beforereq func"""
    uid = request.args.get('login_as')
    if get_user(uid):
        g.user = get_user(uid)


def get_user(uid):
    """ check users """
    if not uid:
        return None
    if int(uid) in users:
        return users[int(uid)]
    return None


@babel.localeselector
def get_locale():
    """get locale function"""
    f = request.args.get('locale')
    if f:
        return f
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """route function"""
    check = 0
    if g.get('user'):
        check = 1
    return render_template("5-index.html", logged=check)


if __name__ == '__main__':
    app.run()
