#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    states_dict = storage.all(State)
    states = list(states_dict.values())
    state_id = None

    if id is not None:
        state = 'State.{}'.format(id)
        if state in states_dict:
            state_id = 1
            states = [states_dict[state]]
    return render_template('9-states.html', states=states, state_id=state_id,
                           id=id)


@app.teardown_appcontext
def closer(err):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
