"""
Functions which manage loading TOS TRD download(s).

Functions which:
    1) Display file selector
    2) Read, with DictReader, the downloaded .csv
    3) Display the OK/Error

Args:
    None, input through dialogs

Returns:
    various - see each function

Raises:
    Exception: none, error are handled through dialogs

"""

from werkzeug.utils import secure_filename
import pathlib
from pathlib import Path
import os
from flask import current_app as app
from collections import OrderedDict


def upload_TOS_download(form_path_data):
    """Upload the previously downloaded TOS TRD .csv file"
        The .csv flie is a flakey format  - sections will be extracted to dict
    """
    # Dict to contain sections from .csv
    sections = {
        'Cash Balance'         : [],
        'Futures Statements'   : [],
        'Forex Statements'     : [],
        'Account Order History': [],
        'Account Trade History': [],
        'Options'              : [],
        'Profits and Losses'   : [],
        'Account Summary'      : []
    }
    sect_names = list(sections) # Keys in order of sections in .csv
    print(f'Keys: {sect_names}')
    fn = secure_filename(form_path_data.filename)
    # cwd = Path.cwd()
    """Get DATABASE_FILE_PATH from config.py; 
        Create dest for uploads: 
            TOS_<date>.csv
            TrRec_<date>_<provider>.csv - provider is IOI, PIA, MMP
    """
    uploads_path = pathlib.Path(app.config['DATABASE_FILE_PATH'])
 #   print(f'uploadsPath: {uploads_path} TOS fn: {fn}')
    fp = uploads_path  /  'TOS_20211115.csv'
    Path(fp).touch()
    form_path_data.save(uploads_path  /  'TOS_20211115.csv')
    with fp.open()  as f:
        sect_id = 0
        in_sect = False
        cur_sect_name = sect_names[sect_id]
        nxt_sect_name = sect_names[sect_id + 1]
        line_count = 0
        for line in f:
            line_count = line_count + 1
            if line_count > 10: break
            if not line.strip() ==  cur_sect_name:
                if in_sect:
                    print(f'cur_sect_name {cur_sect_name} sections[cur_sect_name {sections[cur_sect_name]}  \n')
                    sections[cur_sect_name].append(line)  # value is list of lines
            else:   # Only comes here on section headers
                curr_sect_name = nxt_sect_name
                sect_id  = sect_id  + 1 # Look for next sect id
                nxt_sect_name = sect_names[sect_id]
                in_sect = True  # Stays on after getting to first section
                # print(f'cur_sect_name: {curr_sect_name} in_sect: {in_sect} sect_id: {sect_id} \n')
        # print(f'sections: {sections} \n')
    for key, value in sections.items():   # key is section name; value is list containing the lines in that section
        print(f'\n >>>> Item: {key} \n list {value}')
    # Section names may have blanks - ie: Forex Stuff - translate to Forex_Stuff
        trt = key.maketrans(' ', '_','')
        sect_fn = key.translate(trt)
        print(f'Translated: {sect_fn}')
        with open(uploads_path / sect_fn, 'w') as sect_file:
            sect_file.writelines(value)
        sect_file.close()





def create_TOS_db():
    """Called if db is found not to exist"""
    pass


def TOS_db():
    """
    Wrapper for SQLite3 db
    Calls create_TOS_db() IfNotExist
    :return: connection
    :rtype:
    """
    pass


def select_TOS_download():
    """Display file selector for TOS TRD download"""
    pass


def show_TOS_load_results():
    """Display OK/Error for TOS TRD download"""
    pass
