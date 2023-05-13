from pydantic import BaseModel

# Create your models here.
class Translation(BaseModel):
    input_text = TextField()
    translated_text = TextField()
    source_language = CharField(max_length=10)
    target_language = CharField(max_length=10)
    audio_file = FileField(upload_to='translations/')