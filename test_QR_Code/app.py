"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    """Renders a sample page."""
    return render_template('index.html') 

if __name__ == '__main__':
   
    app.run(debug = True)
