from flask import Flask
import os
import flask_sijax

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')

app = Flask(__name__)
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)

import project.main_app