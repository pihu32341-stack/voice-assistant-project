import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Voice Engine Setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 for Male, 1 for Female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    speak("Hello, I am your Assistant. How can I help you?")
    
    attempts = 0 # Security Fix: Multiple attempts check
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            import datetime
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'shutdown' in query:
            # Flexible security: Ask confirmation instead of direct shutdown
            speak("Are you sure you want to shutdown the system? Say yes to confirm.")
            confirmation = takeCommand().lower()
            if 'yes' in confirmation:
                os.system("shutdown /s /t 1")
            else:
                speak("Shutdown cancelled.")

        elif 'exit' in query:
            speak("Goodbye!")
            break