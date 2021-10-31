from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    email = StringField('E-Mail', validators=[DataRequired()])
    submit = SubmitField('Submit')


class JoinForm(FlaskForm):
    invitation = StringField('Invitation', validators=[DataRequired()])
    submit = SubmitField('Join')
