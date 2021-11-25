from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SubmitField, validators
from flask_wtf.file import (
    FileField, FileAllowed, FileRequired
)

import os

class DownloadForm(FlaskForm):
    """Accept file path for download."""
    path = FileField(
        'Path',
        validators=[
            FileRequired('Full path to downloaded TOS .csv required')
#            FileAllowed(['csv'], 'Must be .csv file')
        ]
    )

    #    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

