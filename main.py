import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests 

# pip install pocketsphinx 

# recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "13180ba55927420bbfccec48e79ce4d7"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        # song = c.lower().split(" ")[2]
        song = c.lower().replace("play","").strip()
        link= musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        # r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code ==200:
            # parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles',[])
            
            # print the headlines
            for article in articles:
                speak(article['title'])


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
    
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r=sr.Recognizer()
    
    
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                  print("Listening...")
                  r.adjust_for_ambient_noise(source, duration=1)
                  audio = r.listen(source , timeout=10, phrase_time_limit=5)
    
            word = r.recognize_google(audio,language="en-IN")
            print(word)
            # if(word.lower()=="jarvis"):
            if "jarvis" in word.lower():
                speak("Ya")
            # print(word)
            #  Listen for command only after jarvis
                with sr.Microphone() as source:
                     print("Jarvis Active...")
                     audio = r.listen(source)
                command = r.recognize_google(audio)   
                processCommand(command) 
            
            
        except Exception as e:
            print("Error; {0}".format(e))
    