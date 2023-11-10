import speech_recognition as sr 
from googletrans import Translator 
from textblob import TextBlob 

recognizer = sr.Recognizer() 
translator = Translator() 

with sr.Microphone() as source: 
    print("Speak something:") 
    audio = recognizer.listen(source) 

try: 
    text = recognizer.recognize_google(audio) 
    print("You said: " + text) 

    translated_text = translator.translate(text, src='en', dest='fr').text 
    print("Translation: " + translated_text) 

    # Perform Sentiment Analysis on the translated text 
    blob = TextBlob(translated_text) 
    sentiment_score = blob.sentiment.polarity 

    if sentiment_score > 0: 
        print("Sentiment: Positive") 
    elif sentiment_score < 0: 
        print("Sentiment: Negative") 
    else: 
        print("Sentiment: Neutral") 

except sr.UnknownValueError: 
    print("Google Web Speech API could not understand the audio.") 
except sr.RequestError as e: 
    print("Could not request results from Google Web Speech API; {0}".format(e)) 