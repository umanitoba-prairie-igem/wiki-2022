# Makes things behave between Windows, Linux and Apple
from os import path
from pathlib import Path

from flask import Flask, render_template
from flask_frozen import Freezer

# make the path to the wiki into a path oject
template_folder = path.abspath('./wiki')

# Instantiates an Instance of the Website
app = Flask(__name__, template_folder=template_folder)
#app.config['FREEZER_BASE_URL'] = environ.get('CI_PAGES_URL')
app.config['FREEZER_DESTINATION'] = 'public'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)


@app.cli.command()
def freeze():
    freezer.freeze()

@app.cli.command()
def serve():
    freezer.run()

# A function that sets the index as the default route, notice the render template function
@app.route('/')
def index():
    return render_template('pages/index.html')

# This deals with every other page, some very clever string formatting going on here
@app.route('/<page>')
def pages(page):
    return render_template(str(Path('pages') / (page.lower() + '.html')))


#This bit let's you run the program with >python app.py, instead of the traditional flask run
# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    app.run(port=8080)

