
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import url_for
from .loadTOS import select_TOS_download, show_TOS_load_results, upload_TOS_download
from .loadTrRec import select_TrRec_download, show_TrRec_load_results
from .config import DevConfig
from .forms import DownloadForm

app = Flask(__name__)
app.config.from_object(DevConfig())

print('app.config: ', app.config)
print('DBFP', app.config['DATABASE_FILE_PATH'])


@app.route('/')
def index():
    return render_template('index.html')    # TODO - Make front page with instructions


@app.route('/loadTOS', methods=['GET', 'POST'])
def loadTOS():
    """
    Present form to download TOS TRD recs .csv file
    Then load those into db
    :return: Success - download report
    :rtype: 
    """

    form = DownloadForm()
    if request.method == 'POST':    #form.validate_on_submit():
        print('POST', form.path.label, form.path, form.path.data)
        upload_TOS_download(form.path.data)
        return redirect(url_for("download_report"))
    return render_template(
        "loadTOS.html",
        form=form,
        template="form-template"
    )
    
    #    msg = 'TOS records will be loaded from file/input_files/TOS'
    # if request.method == 'POST':
    #     render_template('loadTOS.html', select_TOS_download())
    #else:
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
