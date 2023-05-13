from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from .models import Text

class TextForm(FlaskForm):
    text = TextAreaField('Text', validators=[DataRequired()])

    def save(self):
        text = Text(text=self.text.data)
        text.save()
