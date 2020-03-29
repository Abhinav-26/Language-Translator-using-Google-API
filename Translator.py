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


# Here initialising our recorder with hello, whatever after that hello it will recognise it.
if 'hello' in recog1.recognize_google(audio):
    recog1 = spr.Recognizer()
    translator = Translator()        # Translator method for translation
    from_lang = 'en'   # short form of english in which you will speak
    to_lang = 'hi'.    # In which we want to convert, short form of hindi
    with mc as source:
        print("Speak a stentence...")
        audio = recog2.listen(source)  # Storing the speech into audio variable
        get_sentence = recog2.recognize_google(audio) # Using recognize.google() method to convert audio into text.

        # Using try and except block to improve its efficiency.
        try:
            get_sentence = recog2.recognize_google(audio)
            print("Phase to be Translated :"+ get_sentence) # Printing Speech which need to be translated.

            # Using translate() method which requires three arguments, 1st the sentence which needs to be translated
            # 2nd source language and 3rd to which we need to translate in
            text_to_translate = translator.translate(get_sentence, src= from_lang, dest= to_lang)
            text = text_to_translate.text # Storing the translated text in text variable

            # Using Google-Text-to-Speech ie, gTTS() method to speak the the translated text into the destination
            # language which is stored in to_lang. Also, we have given 3rd argument as False because by default it
            # speaks very slowly and we don't want it to happen.
            speak = gTTS(text=text, lang=to_lang, slow= False)

            # Using save() method to save the translated speech in capture_voice.mp3.
            # You can use any name to save the file.
            speak.save("captured_voice.mp3")
            os.system("start captured_voice.mp3")  # Using OS module to run the translated voice.

        # Here we are using except block for UnknownValue and Request Error and printing the same to provide better
        # service to the user.
        except spr.UnknownValueError:
            print("Unable to Understand the Input")
        except spr.RequestError as e:
            print("Unable to provide Required Output".format(e))
