
from project import app
from flask import render_template
from flask import Flask, g
import flask_sijax

import pandas as pd
import re
import os
from os import listdir
from os.path import isfile, join
import json


@app.route('/')
def words():

    return "hello world!"#render_template("index_main.html")
