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
from werkzeug.utils import secure_filename, FileStorage
from pathlib import Path
import os

def upload_TOS_download(form_path_data):
    """Upload the previously downloaded TOS TRD .csv file"""
    fn = secure_filename(form_path_data.filename)
    cwd = Path.cwd()
    """Get DATABASE_FILE_PATH from config.py; 
        Create dest for upload: TOS_<date>.csv
    """
    print(f'TOS filename: {fn}')
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
