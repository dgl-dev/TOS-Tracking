
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import url_for
from loadTOS import select_TOS_download, show_TOS_load_results
from loadTrRec import select_TrRec_download, show_TrRec_load_results


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')    # TODO - Make front page with instructions


@app.route('/loadTOS', methods=['GET', 'POST'])
def loadTOS():
    #    msg = 'TOS records will be loaded from file/input_files/TOS'
    if request.method == 'POST':
        return select_TOS_download()
    else:
        return show_TOS_load_results()
#        return render_template('loadTOS.html')


@app.route('/loadTrRec', methods=['GET', 'POST'])
def loadTrRec():
    if request.method == 'POST':
        return select_TrRec_download()
    else:
        return show_TrRec_load_results()
    return render_template('loadTrRec.html')


@app.route('/reports', methods=['GET', 'POST'])
def reports():     # dates (from,to)
    if request.method == 'POST':
        return select_report()
    else:
        return show_report_results()
    return render_template('reports.html')
