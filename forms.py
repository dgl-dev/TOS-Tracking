from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField,
    TextAreaField,
    SubmitField,
    PasswordField,
    DateField,
    SelectField
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    URL
)

class DownloadForm(FlaskForm):
    """Accept file path for download."""
    path = StringField(
        'Path',
        validators=[
            DataRequired()
        ]
    )

#    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')