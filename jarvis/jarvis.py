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
import time
import pywhatkit as pwk
import pyautogui

from parts .setting import *


# from save import *


# data = open("save.py", "w")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[voice_num].id)
engine.setProperty('rate', 220)


translator = Translator()


def speak(audio):
    audio_hi = translator.translate(audio, dest =input_lang).text
    engine.say(audio_hi)
    engine.runAndWait()
    print(audio)



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









############# CREATING DATABASE FOR SAVING NAME ############




filename = "./database/data1.json"

with open(filename, "r") as f:
    temp = json.load(f)
    i=0
    for entry in temp:
        name = entry["name"]
        i=i+1


def view_data():
    with open(filename, "r") as f:
        temp = json.load(f)
        i=0
        for entry in temp:
            name = entry["name"]
            # print(name)
            # print("\n\n")
            i=i+1





def edit_data():
    view_data()
    new_data = []
    with open(filename, "r") as f:
        temp = json.load(f)
    # print("Which index number would you like to delete?")
    edit_option = 0
    i = 0
    for entry in temp:
        if i == int(edit_option):
            name = (entry["name"])
            print(f"Current Name of owner : {name}")
            speak("What would you like the new name to be?: ")
            # name = takeCommand()
            name = takeCommand()
            new_data.append({"name": name})
            i=i+1
        else:
            new_data.append(entry)
            i=i+1
        with open(filename, "w") as f:
            json.dump(new_data, f, indent=4)


############################ END ##############################

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    
    speak(f"I am {name}'s voice assistant. Please tell me how may I help you")       





webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))



if __name__ == "__main__":

    # speak("What should i call you")
    # master = takeCommand()
    # print(master)
    
    wishMe()

    print(name)

    
    while True:
    # if 1:
    
        query = takeCommand().lower()


        if 'wake up' in query or 'jarvis' in query or 'help jarvis' in query:

            seconds = 600 #The amount of seconds i want the loop to execute 
            end_time = time.time() + seconds
            while time.time() < end_time:
                print("This loop will execute for 60 seconds")
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
                    webbrowser.get('chrome').open('youtube.com')

                elif 'open google' in query:
                    webbrowser.get('chrome').open('google.com')

                elif 'open stackoverflow' in query:
                    webbrowser.get('chrome').open('stackoverflow.com')  




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
                    with open(filename, "r") as f:
                        temp = json.load(f)
                        i=0
                        for entry in temp:
                            name = entry["name"]
                            i=i+1
                    speak(f"Your name is {name}. my lord")

                
                elif 'change the name' in query:

                    edit_data()
                    








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
                        speak("Sorry my friend "+ name +" . I am not able to send this email")    



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
                        speak("Sorry my friend "+ name +" . I am not able to send this email")    


                elif 'test' in query:
                    speak("start the test")
                    takeCommand()
                    speak("I don't know anything about this")
                
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
                    # playsound("C:\Users\Dell\OneDrive\Desktop\jarvis\songs\sound effect.mp3")
                    exit()

                elif 'send message' in query:
                    speak("What is the contact number")
                    contact_num = takeCommand().lower().replace(" ", "")
                    if contact_num == 'anjali':
                        contact_num = '7838604065'
                    elif contact_num == 'jagdish':
                        contact_num = '9968524801'
                    speak("What is the message")
                    message = takeCommand()
                    pwk.sendwhatmsg_instantly("+91"+contact_num, message, 10, True,  10)

                # elif 'search in google' in query:
                elif 'search' in query and 'google' in query:
                    speak("What do you want to search")
                    search = takeCommand()
                    pwk.search(search)
                

                elif 'search' in query and 'information' in query:
                    speak("What information do you want")
                    search_info = takeCommand()
                    # speak("In how much lines you want the information")
                    # lines = takeCommand()
                    pwk.info(search_info, lines = 4)
                    print("\n\nSuccessfully Searched")


                elif 'search' in query and 'youtube' in query:
                    speak("what do you want to search")
                    youtube_search = takeCommand()
                    webbrowser.get('chrome').open('youtube.com')
                    time.sleep(10)
                    # pyautogui.click()
                    pyautogui.press('/')
                    time.sleep(1)
                    pyautogui.write(youtube_search)
                    time.sleep(1)
                    pyautogui.press('enter')
                    


                elif 'change my language' in query:
                    speak("what is the language you want")
                    input_lang = takeCommand().lower()
                    if input_lang == "hindi":
                        input_lang = "hi"
                        voice_num = int("2")
                        speak("langauge sucessfully changed")
                    elif input_lang == "english":
                        input_lang = "en"
                        voice_num = int("0")
                        speak("langauge sucessfully changed")
                    

                elif 'friend' in query or 'hello' in query or "jarvis" in query:
                    speak("hi, how are you")



                # elif 'de some calculation' or 'can you calculate' in query:
                #     speak("what do you want to calculate?")
                #     my_string = takeCommand()
                #     print(my_string)
                #     def get_operator_fn(op):
                #         return{
                #             '+': operator.add,
                #             '-': operator.sub,
                #             '*': operator.mul,
                #             'divide': operator.__truediv__,
                #         }[op]
                #     def eval_binary_expr(op1, oper, op2):
                #         op1,op2 = int(op1),int(op2)
                #         return get_operator_fn(oper)(op1,op2)
                #     speak("Your result is")
                #     speak(eval_binary_expr(*(my_string.split())))



