from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)],
                       render_kw={'placeholder': 'Your name', 'class': 'form-control'})
    surname = StringField('Surname', validators=[DataRequired(), Length(max=50)],
                          render_kw={'placeholder': 'Your surname', 'class': 'form-control'})
    email = StringField('Email', validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'Your email', 'class': 'form-control', 'type': 'email'})
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=300)],
                            render_kw={'placeholder': 'Your message', 'class': 'form-control', 'rows': '3'})