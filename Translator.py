# Importing necessary modules required

import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

# Creating Recogniser() class object
recog1 = spr.Recognizer()
recog2 = spr.Recognizer()

# Creating microphone instance with device microphone whose index value is zero
mc = spr.Microphone(device_index=0)

# Capture Voice
with mc as source:
    print("Speak 'hello' to initiate the Translation !")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    audio = recog1.listen(source)
