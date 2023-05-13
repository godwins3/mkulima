from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class TranslationForm(FlaskForm):
    input_text = StringField(widget=TextArea(), render_kw={'placeholder': 'Enter text to translate'})
    target_language = SelectField(choices=[('en', 'English'), ('es', 'Spanish'), ('fr', 'French'), ('de', 'German')], default='en')
    audio_file = FileField()

