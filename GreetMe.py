import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <= 12:
        speak("Good Morning,sir")
    elif hour > 12 and hour <= 18:
        speak("Good Afternoon,sir")

    else:
        speak("please tell me,How can I help you?")
            

