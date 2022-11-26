import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from googletrans import Translator
from playsound import playsound

from parts .setting import *

# from save import *


# data = open("save.py", "w")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[voice_num].id)
engine.setProperty('rate', 160)


translator = Translator()


def speak(audio):
    audio_hi = translator.translate(audio, dest =input_lang).text
    engine.say(audio_hi)
    engine.runAndWait()
    print(audio)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am GJ's voice assistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query_en = r.recognize_google(audio, language=input_lang)
        query = translator.translate(query_en, dest="en").text
        print(f"User said: {query_en}\n")
        print(f"translated: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gauravjo9968@gmail.com', '23122312')
    server.sendmail('gauravjo9968@gmail.com', to, content)
    server.close()



    

if __name__ == "__main__":

    # speak("What should i call you")
    # master = takeCommand()
    # print(master)
    
    wishMe()



    
    while True:
    # if 1:
    
        query = takeCommand().lower()

        # Logic for executing tasks based on query
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

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'music' in query:
            
            # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            music_dir = 'C:\\Users\\Dell\OneDrive\\Desktop\\JARVIS\\songs'
            songs = os.listdir(music_dir)
            print(songs)   
            try:
                speak("Which one")
                num = takeCommand()
                converted_num = int(num)
                os.startfile(os.path.join(music_dir, songs[converted_num - 1])) 
            except Exception as e:
                print(e)
                speak("Sorry my friend Gaurav Joshi. I am not able to play the song")   
        
        elif 'my name' in query:


            if master == "None":
                speak("What is your name?")
                master = takeCommand()
                print(master)
            else:
                speak("Your name is " + master + ". my lord")

            # speak("Your name is " + master + ". my lord")


        elif 'play song' in query:
            # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            fav_music = 'C:\\Users\\Dell\OneDrive\\Desktop\\JARVIS\\songs\\demons.mp4'
  
            os.startfile(fav_music)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend "+ master +" . I am not able to send this email")    



        elif 'email to new user' in query:
            try:
                speak("who is the user")
                user = takeCommand()
                speak("What is the content")
                content = takeCommand()
                to = user + "@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend "+ master +" . I am not able to send this email")    


        elif 'test' in query:
            speak("start the test")
            takeCommand()
            print("I don't know anything about this")
        
        elif 'turn off the pc' in query:
            speak("are you sure")
            shutdown = takeCommand().lower()
            if shutdown == 'no':
                exit()
            elif shutdown == 'yes':
                os.system("shutdown /s /t 1")
            else :
                speak("I didn't understand what do you want")
        
        elif 'destroy yourself' in query:
            speak("Self destructing in. 5 . 4 . 3 . 2 . 1")
            playsound("sound effect.mp3")
            exit()

        elif 'change my language' in query:
            speak("what is the language you want")
            lang_change = takeCommand()
            


