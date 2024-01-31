#!/usr/bin/python3
"""A python script that starts a Flask web application"""


from flask import Flask

# This creates an instance called app of the class by passong the __name__ variable
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """This displays "Hello HBNB!"

    Returns:
        str: text on the index page
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    """This displays "HBNB"

    Returns:
        str: text on the page
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True)
