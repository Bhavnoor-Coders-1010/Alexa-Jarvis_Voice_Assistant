#Importing Necessary Libraries
'''
After installing all the packages, you might face a problem saying that pyaudio is not installed.
Solution:
Step 1: Go to CMD(command prompt).
Step 2: Type pip install pipwin and wait until pipwin is installed.
Step 3: Now, type pipwin install PyAudio.
Step 4: Now, PyAudio will be installed.
'''
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wp
import webbrowser as wb
import os
import random
import pyautogui as pg
import csv
import smtplib as sl
import time
import screen_brightness_control as sbc
#Putting all my e-mail contacts into a dictionary with their names as the keys and e-mails as values
contacts = {}
filename = "contacts - contacts.csv"
with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        contacts.update(line)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
x = 0
#print(voices[0].id)
engine.setProperty('voice', voices[x].id)
def speak(audio):
    def speak_main():
        engine.say(audio)
        engine.runAndWait()
    speak_main()
def wishMe():
    hour  = int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak("Good Morning!!")
    elif 12<=hour<=15:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")
    if x == 1:
        speak("I am Anna, your virtual assistant!!")
    else:
        speak("I am Jarvis, your virtual assistant!!")
    speak("What Can I do for you?")
def takeCommand():
    '''
    Takes input from the
    microphone of the user
    and outputs a string
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)

        print("Could you please repeat that again?")
        return "None"
    return query
def sendEmail(to, content):
    server = sl.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("__Your_E-Mail_id__", "__Password__")
    server.sendmail("__Your_E-Mail_id__", to, content)
    server.close()
#Main functions that run...
if __name__ == '__main__':
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'thank you' in query or 'thanks a lot' in query:
            speak("My pleasure sir!")
        elif 'very good' in query or 'you are great' in query:
            speak("Thank You sir!")
        elif 'quit' in query or 'bye' in query or 'exit' in query or 'see you soon' in query:
            print("Have a nice day Sir!")
            speak("Have a nice day sir!")
            exit()
        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wp.summary(query, sentences = 1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube and search for 'in query:
            wb.open("https://www.youtube.com/results?search_query=" + query.replace("open youtube and search for ", ""))
        elif 'search youtube for' in query:
            wb.open("https://www.youtube.com/results?search_query=" + query.replace("search youtube for ", ""))
        elif 'search for' in query:
            wb.open(f"https://www.google.com/search?q=" + query.replace('search for',''))
        elif 'open youtube' in query:
            wb.open("https://www.youtube.com/")
        elif 'open amazon' in query:
            wb.open("https://www.amazon.com/")
        elif 'open google' in query:
            wb.open("https://www.google.com")
        elif 'open stackoverflow' in query or 'open stack overflow' in query:
            wb.open("https://www.stackoverflow.com")
        elif 'open crazy games' in query or 'open crazygames' in query:
            wb.open("https://www.crazygames.com")
        elif 'open geeksforgeeks' in query or 'open geeks for geeks' in query:
            wb.open("https://www.geeksforgeeks.org")
        elif 'open teams' in query or 'open team' in query:
            wb.open("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:7bbcd8f3a3b64bcb8d41e1867a1546f0@thread.tacv2&ctx=channel")
        elif 'open discord' in query:
            wb.open("https://discord.com/channels/750904002178318427/751656533775089794")
        elif 'play music' in query:
            music_dir = "C:\\Users\\Bhavnoor Singh\\Desktop\\Sample Music _2"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.choice(range(0,len(songs)))]))
        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H: %M: %S")
            print(strTime)
            speak(f"Sir, The time is {strTime}")
        elif 'brightness' in query:
            s = ''
            for i in query:
                if i.isnumeric():
                    s+=i
            sbc.set_brightness(s)
        elif 'from windows open' in query:
            query = query.replace("from windows open", "")
            speak(f"Opening {query}")
            pg.click(10,1070, duration = 1 )
            time.sleep(2)
            pg.typewrite(query, interval = 0.5)
            pg.hotkey('enter')
        elif 'click my picture' in query:
            pg.click(10,1070, duration = 1 )
            time.sleep(2)
            pg.typewrite("camera", interval = 0.5)
            pg.hotkey('enter')
            time.sleep(5)
            speak("Please pose for your picture!")
            for i in range(5,0,-1):
                speak(i)
            pg.hotkey("enter")
            time.sleep(2)
            pg.hotkey("tab")
            time.sleep(2)
            pg.hotkey("enter")
            speak("This is your picture!")
        elif 'send email to' in query:
            query = query.replace("send email to ", "")
            # print(query)
            try:
                speak("What should I say?")
                content = takeCommand()
                to = contacts.get(query)
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I was not able to send this email.")

        elif 'how are you' in query:
            speak("I am good and at your service Sir. How are you?")
            ans = takeCommand()
            if 'good' in ans or 'fine' in ans or 'great' in ans:
                speak("That's great sir!!")
            elif 'sad' in ans or "not good" in ans:
                speak("What happened sir?")
                ans_2 = takeCommand()
                if 'nothing much' in ans_2 or 'leave it' in ans_2 or "don't want to discuss" in ans_2:
                    speak("Ok Sir!")
                else:
                    speak("Everything will be okay sir!")
            elif 'okay' in ans or 'ok' in ans:
                speak("Let me make you happier sir!")
                speak("You may wish to listen to some songs!")
                music_dir = "C:\\Users\\Bhavnoor Singh\\Desktop\\Sample Music _2"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[random.choice(range(0, len(songs)))]))

        elif 'send message to' in query:
            query1 = query.split()
            rcp = query1[3]
            del query1[:query1.index("say") + 1]
            query_final = str(' '.join(query1))
            time.sleep(2)
            wb.open("https://web.whatsapp.com")
            time.sleep(30)
            pg.hotkey('tab')
            pg.typewrite(rcp)
            pg.hotkey("enter")
            time.sleep(5)
            pg.typewrite(query_final)
            pg.hotkey("enter")
        elif 'say' in query:
            query_1 = query.split()
            query_1.remove("say")
            query__final = str(' '.join(query_1))
            speak(query__final)