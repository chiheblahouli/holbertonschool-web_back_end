#!/usr/bin/env python3
"""second app"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ config class"""
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """route function"""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run()
