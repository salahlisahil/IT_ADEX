from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, Length


class CommentForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired(), Length(max=100)],
                       render_kw={'placeholder': 'Your fullname', 'class': 'form-control'})
    header = StringField('Review Header', validators=[DataRequired(), Length(max=100)],
                          render_kw={'placeholder': 'Review header', 'class': 'form-control'})
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=1000)],
                            render_kw={'placeholder': 'Your message', 'class': 'form-control', 'rows': '3'})
