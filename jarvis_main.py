import pyttsx3
import speech_recognition 
from plyer import notification
from pygame import mixer
engine = pyttsx3.init("sapi5")   #for windows
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Command():   ##takeCommand
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 320
        audio = r.listen(source,0,5)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
    HEAD
## For alarm 
def alarm():
     timehere = open()



    
if __name__ == "__main__":
    while True:
        query = Command().lower()

        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:

                query = Command().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")


        elif "google" in query:
               from SearchNow import searchGoogle
               searchGoogle(query)
        elif "youtube" in query:
                from SearchNow import searchYoutube
                searchYoutube(query)
        elif "wikipedia" in query:
                from SearchNow import searchWikipedia
                searchWikipedia(query)
  
        elif "finally sleep" in query:
                speak("Going to sleep,sir")
                exit()
         
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    exit() #break


                # schedule my day 

        elif "schedule my day" in query:
            tasks = [] #Empty list 
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = Command().lower()
            if "yes" in query:
                file = open("tasks.txt","w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                 tasks.append(input("Enter the task :- "))
                file = open("tasks.txt","a")
                file.write(f"{i}. {tasks[i]}\n")
                file.close()
        elif "show my schedule" in query:
             file  = open("tasks.txt","r")
             content = file.read()
             file.close()
             mixer.init()
             mixer.music.load("noti.mp3")
             mixer.music.play()
             notification.notify(
                title = "my schedule :-",
                message = content,
                timeout = 15
             )


             
    import pyttsx3
import speech_recognition 
import requests
from plyer import notification
from pygame import mixer

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 180)

class Jarvis:
    def __init__(self):
        self.api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'
        self.units = 'metric'  # You can change this to 'imperial' for Fahrenheit

    def speak(self, audio):
        engine.say(audio)
        engine.runAndWait()

    def get_weather(self, city):
        params = {'q': city, 'appid': self.api_key, 'units': self.units}
        response = requests.get(self.base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
        else:
            return f"Unable to fetch weather data for {city}."

    def command(self):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 320
            audio = r.listen(source, 0, 5)

        try:
            print("Understanding..")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")

            # Check for weather command
            if "weather in" in query:
                city = query.split("weather in")[1].strip()
                return self.get_weather(city)

        except Exception as e:
            print("Say that again")
            return "None"

import pyttsx3
import speech_recognition 
import requests
from plyer import notification
from pygame import mixer

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 180)

class Jarvis:
    def __init__(self):
        self.api_key = '1a1fd2aa3610e75f26058abf4483ccad'
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'
        self.units = 'metric'  # You can change this to 'imperial' for Fahrenheit

    def speak(self, audio):
        engine.say(audio)
        engine.runAndWait()

    def get_weather(self, city):
        params = {'q': city, 'appid': self.api_key, 'units': self.units}
        response = requests.get(self.base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
        else:
            return f"Unable to fetch weather data for {city}."

    def command(self):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listening.....")
            r.pause_threshold = 1
            r.energy_threshold = 320
            audio = r.listen(source, 0, 5)

        try:
            print("Understanding..")
            query = r.recognize_google(audio, language='en-in')
            print(f"You Said: {query}\n")

            # Check for weather command
            if "weather in" in query:
                city = query.split("weather in")[1].strip()
                return self.get_weather(city)

        except Exception as e:
            print("Say that again")
            return "None"

if __name__ == "__main__":
    jarvis = Jarvis()

    while True:
        response = jarvis.command()
        if response:
            print("Jarvis:", response)
            jarvis.speak(response)

