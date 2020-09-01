#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

hbnb = Flask(__name__)
hbnb.url_map.strict_slashes = False


@hbnb.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@hbnb.route('/hbnb')
def hbnb_hbnb():
    return 'HBNB'


@hbnb.route('/c/<text>')
def c_text(text):
    return 'C {}'.format(text.replace('_', ' '))


@hbnb.route('/python')
@hbnb.route('/python/<text>')
def python_text(text='is_cool'):
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    hbnb.run(host='0.0.0.0', port=5000)
