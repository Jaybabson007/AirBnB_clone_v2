#!/usr/bin/python3
"""A python script that starts a Flask web application"""


# import Flask class from flask module
# import render_template for rendering templates to browser
# fetch data from storage engine
from flask import Flask, render_template

from models import storage

# This creates an instance called app of the class by passong the __name__ variable
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception=None):
    """This function removes the current SQLAlchemy Session
    """
    if storage is not None:
        storage.close()


@app.route('/states')
@app.route('/states/<state_id>')
def states(state_id=None):
    """This displays a HTML page: inside the tag BODY"""
    states = storage.all("State")
    if state_id is None:
        return render_template('9-states.html', states=states)
    state = states.get('State.{}'.format(state_id))
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(debug=True)
