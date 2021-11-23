from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField, TextAreaField 
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired(), Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Enviar')

