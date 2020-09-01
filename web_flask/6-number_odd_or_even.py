#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template

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


@hbnb.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)


@hbnb.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@hbnb.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    hbnb.run(host='0.0.0.0', port=5000)
