import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from googletrans import Translator
from playsound import playsound
import json










translator = Translator()


def speak(audio):
    audio_hi = translator.translate(audio, dest ="en").text
    engine.say(audio_hi)
    engine.runAndWait()
    print(audio)





# data = open("save.py", "w")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 220)



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
        query_en = r.recognize_google(audio, language="en")
        query = translator.translate(query_en, dest="en").text
        print(f"User said: {query_en}\n")
        print(f"translated: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query







filename = "./database/data1.json"



def view_data():
    with open(filename, "r") as f:
        temp = json.load(f)
        i=0
        for entry in temp:
            name = entry["name"]
            print(name)
            print("\n\n")
            i=i+1





def edit_data():
    view_data()
    new_data = []
    with open(filename, "r") as f:
        temp = json.load(f)
    print("Which index number would you like to delete?")
    edit_option = 0
    i = 0
    for entry in temp:
        if i == int(edit_option):
            name = (entry["name"])
            print(f"Current Name of King : {name}")
            speak("What would you like the new name to be?: ")
            # name = takeCommand()
            name = input("New name is:\n")
            new_data.append({"name": name})
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
        with open(filename, "w") as f:
            json.dump(new_data, f, indent=4)











    

if __name__ == "__main__":

    # speak("What should i call you")
    # master = takeCommand()
    # print(master)




    
    while True:
    # if 1:
    
        # query = takeCommand().lower()
        check = input("Type command here:")

        # Logic for executing tasks based on query
        if 'wikipedia' in check:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'my name' in check:

            # Choices()
            # choice = input("\nEnter Number: ")
            # if choice == '1':
            #     view_data()
            # elif choice == '2':
            #     add_data()
            # elif choice == '3':
            #     delete_data()
            # elif choice == '4':
            #     edit_data()
            # else:
            #     print("You did not select a number, please read more carefully.")


            # with open(filename, "r") as f:
            #     data = json.load(f)
            #     name_data = (data["names"])
            #     for i in name_data:
            #         name = (i["name"])
            #         print(name)

        
            with open(filename, 'r') as f:
                temp = json.load(f)
                i = 0
            for entry in temp:
                name = entry["name"]
                print(f"Name of King : {name}")
                print("\n\n")
                i=i+1
                speak(f"Your name is {name}. my lord")

            # speak("Your name is " + master + ". my lord")
        
        elif 'change the name' in check:
            edit_data()

