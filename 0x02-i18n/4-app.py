#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Bebel config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_local():
    """
    configure app based on local languages
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index() -> str:
    """"
    Base routing
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
