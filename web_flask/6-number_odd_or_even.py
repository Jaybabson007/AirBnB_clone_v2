#!/usr/bin/python3
"""A python script that starts a Flask web application"""

from flask import Flask, render_template

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


@app.route('/c/<text>')
def c_route(text):
    """This displays "C", followed by the value of the text variable

    Args:
        text (str): text to be served on the page

    Returns:
        str: text on the page
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    """This display "Python", followed by the value of the text variable

    Args:
        text (str): text to be served on the page

    Returns:
        str: text on the page
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n):
    """This displays "n is a number" only if n is an integer

    Args:
        n (integer): number to be displayed on page

    Returns:
        str: text on the page
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template_route(n):
    """This displays a HTML page only if n is an integer

    H1 tag: "Number: n" inside the tag BODY

    Args:
        n (integer): number to be displayed on page

    Returns:
        str: text on the page
    """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even_route(n):
    """This displays a HTML page only if n is an integer

    Args:
        n (integer): number to be displayed on page

    Returns:
        str: text on the page
    """
    if n % 2 == 0:
        condition = 'even'
    else:
        condition = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           condition=condition)


if __name__ == '__main__':
    app.run(debug=True)
