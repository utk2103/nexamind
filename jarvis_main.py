import pyttsx3
import speech_recognition 
engine = pyttsx3.init("sapi5")
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
<<<<<<< HEAD
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
                    break 

