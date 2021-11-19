
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')    # TODO - Make front page with instructions


@app.route('/loadTOS')
def loadTOS():
    return render_template('loadTOS.html')


@app.route('/loadRecc')
def loadRecc():
    return render_template('loadRecc.html')


@app.route('/reports')
def reports():     # dates (from,to)
    return render_template('reports.html')
