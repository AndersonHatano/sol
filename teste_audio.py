import os
from gtts import gTTS

#options
text_to_read = 'Meu nome é sol'
language = 'pt'
slow_audio_speed = False
filename = "my_file.mp3"


def reading_from_string(frase):
    audio_created = gTTS(text=frase, lang=language, slow=slow_audio_speed)
    audio_created.save(filename)

    os.system(f'start {filename}')


if __name__ == "__main__":
    reading_from_string()