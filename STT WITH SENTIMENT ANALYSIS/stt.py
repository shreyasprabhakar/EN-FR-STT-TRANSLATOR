import speech_recognition as sr
from googletrans import Translator

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Web Speech API; {0}".format(e))

translator = Translator()
translated_text = translator.translate(text, src='en', dest='fr').text
print("Translation: " + translated_text)
