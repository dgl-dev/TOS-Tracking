
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
    return('<h1>Loading TOS TRD Records</h1>')


@app.route('/loadRecc')
def loadRecc():
    return('<h1>Loading Trading Recommendations</h1>')


@app.route('/reports')
def reports(dates):     # dates (from,to)
    return('<h1>Loading Trading Report</h1>')
