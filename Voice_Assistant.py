import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wp
from playsound import playsound
import webbrowser as wb
import os
import random
import pyautogui as pg
import csv
import smtplib as sl
import time
import screen_brightness_control as sbc
import pywhatkit as kit
import cv2

# import googletrans
# import turtle
# import cv2
# import threading
#contacts = {}
#filename = "contacts - contacts.csv"
#with open(filename, 'r') as data:
#    for line in csv.DictReader(data):
#        contacts.update(line)


# def whatsapp_contacts(contact):
#     for i in nums.keys():
#         if contact in i.split():
#             return nums[i]
#         else:
#             raise Exception("Num Error: Number not in your contacts")
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# wb = webbrowser.get(chrome_path)

# def timer():
#     hours = int(input("Enter hours for the timer: "))
#     minutes = int(input("Enter minutes for the timer: "))
#     seconds = int(input("Enter seconds for the timer: "))
#
#     t1 = turtle.Turtle()
#     t1.hideturtle()
#     screen1 = t1.getscreen()
#     screen1.bgcolor("#39FF14")
#     h = str(hours)
#     m = str(minutes)
#     s = str(seconds)
#
#     while True:
#         t1.clear()
#         t1.write("Total Time: " + h.zfill(2) + ":" + m.zfill(2) + ":" + s.zfill(2), align = "center", font=("courier", 25, "normal"))
#         t1.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2), align = "center", font = ("courier", 90 ,"normal"))
#         seconds -= 1
#         time.sleep(1)
#         if seconds == -1:
#             minutes -= 1
#             seconds = 59
#         if minutes == -1:
#             hours -= 1
#             minutes = 59
#         if hours == -1:
#             break


# cap = cv2.VideoCapture('VA.mp4')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
global x
x = 1
# VA = input("Alexa or Jarvis?")
# if 'alexa' in VA.lower():
#     x = 1
# else:
#     x = 0
#print(voices[0].id)
engine.setProperty('voice', voices[x].id)
def speak(audio):
    def speak_main():
        engine.say(audio)
        engine.runAndWait()
    # def robo():
    #     if (cap.isOpened() == False):
    #         print("Error opening video stream or file")
    #
    #     while (cap.isOpened()):
    #         ret, frame = cap.read()
    #         if ret == True:
    #
    #             cv2.imshow('Frame', frame)
    #
    #             if cv2.waitKey(25) & 0xFF == ord('q'):
    #                 break
    #
    #         else:
    #             break
    #
    #     cap.release()
    #
    #     cv2.destroyAllWindows()
    # sm1 = speak_main()
    # r1 = robo()
    # sm = threading.Thread(target=sm1.run, args=())
    # r = threading.Thread(target=r.run, args = ())
    # sm.start()
    # r.start()
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
        speak("I am Alexa, your virtual assistant!!")
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
        r.pause_threshold = 0.5
        r.energy_threshold =  600
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    except:
        print("Could you please repeat that again?")
        return "None"
    return query
def sendEmail(to, content):
    server = sl.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("singh.bhavnoor.4854@gmail.com", "2191419191@BSNss^&WJKKWJKF@meherkaro@BABAji")
    server.sendmail("singh.bhavnoor.4854@gmail.com", to, content)
    server.close()
whatsapp_contacts = {"papa" : "919711117489","aryan":"919971828986","bhavna":"918802848358","bhavnoor":"919899835666"}
#speak("Running")

if __name__ == '__main__':
    while True:
        #query__1 = takeCommand().lower()
        if True:

            wishMe()

            while True:
                query = takeCommand().lower()
                if ' dot ' in query:
                    query = query.replace(' dot ',".")

                if 'thank you' in query or 'thanks' in query:
                    playsound(os.path.join("C:\\Users\\Bhavnoor Singh\\Desktop\\Bhavnoor Singh\\Sample Music _2\\Voice 005.mp3"))
                    # time.sleep(8)
                    # os.path.join("C:\\Users\\Bhavnoor Singh\\Desktop\\\Bhavnoor Singh\\Sample Music _2\\Voice 005.m4a").close()
                elif 'what can you do' in query:
                    speak("I can search on wikipedia, youtube, google and I can send mail, send a message and many more!!!")
                    print(
                        "I can do the following things:\n1) Search on wikipedia, youtube, google.\n2) Open google, youtube, amazon ,Crazy Games, Stack Overflow, GeeksForGeeks, Microsoft Teams, Discord, WhatsApp\n3) Join your chemistry or VMC Class\n4) Set Timer\n5) Play Music\n6) Tell the time\n7) Change screen Brightness\n8) open anything you say from windows\n8) Click your picture\n9) Send E-Mail\n10) Send message\n11) Say anything you want me to say!"
                    )

                elif 'good' in query or 'very good' in query or 'you are great' in query:
                    speak("Thank You sir!")
                
                elif 'quit' in query or 'bye' in query or 'exit' in query or 'see you soon' in query:
                    byee = ['Have a nice day!', "Adios Amigos", "Until next time!", "See you soon!"]
                    byeee = random.choice(byee)
                    print(byeee)
                    speak(byeee)
                    exit()
                elif 'wikipedia' in query:
                    speak("Searching wikipedia...")
                    query = query.replace("wikipedia", "")
                    results = wp.summary(query, sentences = 1)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                #elif 'search wikipedia for' in query:
                #    speak("Searching wikipedia...")
                #    query = query.replace('search wikipedia for', "")
                #    results = wp.summary(query, sentences = 1)
                #    speak("According to Wikipedia")
                #    print(results)
                #    speak(results)
                #elif 'search wikipedia' in query:
                #    speak("Searching wikipedia...")
                #    query = query.replace("search wikipedia", "")
                #    results = wp.summary(query, sentences = 1)
                #    speak("According to Wikipedia")
                #    print(results)8
                #    speak(results)
                elif 'open youtube and search for 'in query:
                    speak("Searching youtube for " + query.replace("open youtube and search for ", ""))
                    wb.open("https://www.youtube.com/results?search_query=" + query.replace("open youtube and search for ", ""))
                elif 'search youtube for' in query:
                    speak("Searching youtube for " + query.replace("search youtube for ", ""))
                    wb.open("https://www.youtube.com/results?search_query=" + query.replace("search youtube for ", ""))
                elif 'from youtube play' in query:
                    speak("Playing" + query.replace("from youtube play ", ""))
                    kit.playonyt(query.replace("from youtube play ", ""))
                #elif 'click screenshot' in query:
                    #img = pg.screenshot(f"Alexa_SS_{datetime.datetime.now()}")
                    #speak("Screenshot clicked!")

                    
                    
































                
                elif 'search for' in query:
                    for i in query.split():
                        try:
                            if i == 'search' and query.split()[query.split().index(i)+1]=='for':
                                search_query = ' '.join(query.split()[(query.split().index(i)+2):])
                                speak(f"Searching for {search_query}")
                                wb.open(f"https://www.google.com/search?q={search_query}")
                                break
                        except:
                            continue
                
                

























                elif 'open youtube' in query:
                    speak("Opening Youtube")
                    wb.open("https://www.youtube.com/")
                elif 'open amazon' in query:
                    speak("Opening Amazon")
                    wb.open("https://www.amazon.com/")
                elif 'open google' in query:
                    speak("Opening Google")
                    wb.open("https://www.google.com")
                elif 'open stackoverflow' in query or 'open stack overflow' in query:
                    speak("Opening StackOverflow")
                    wb.open("https://www.stackoverflow.com")
                elif 'open' in query:
                    for i in query.split():
                        if ('.com' in i) or ('.co.in' in i) or ('.org' in i) or ('.co' in i) or ('.in' in i):
                            speak(f'opening {i}')
                            wb.open(i)
                            break
                    
                elif 'open teams' in query or 'open team' in query:
                    speak("Opening Teams")
                    wb.open("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:7bbcd8f3a3b64bcb8d41e1867a1546f0@thread.tacv2&ctx=channel")
                elif 'open discord' in query:
                    speak("Opening Discord")
                    wb.open("https://discord.com/channels/750904002178318427/751656533775089794")


                elif 'timer' in query:
                    hours = int(input("Enter hours for the timer: "))
                    minutes = int(input("Enter minutes for the timer: "))
                    seconds = int(input("Enter seconds for the timer: "))
                    time.sleep(hours*3600 + minutes*60 + seconds)
                    for i in range(10):
                        speak("Wake Up!!!")
                        time.sleep(0.10)

                elif 'play music' in query or 'bored' in query:
                    music_dir = "C:\\Users\\Bhavnoor Singh\\Desktop\\Bhavnoor Singh\\Sample Music _2\\Songs I like"
                    songs = os.listdir(music_dir)
                    speak("Playing Music")
                    os.startfile(os.path.join(music_dir, songs[random.choice(range(0,len(songs)))]))
                elif 'who is your creator' in query:
                    speak("My Creator is Bhavnoor Singh!!")
                elif "what's the time" in query or 'what is the time' in query:
                    strTime = datetime.datetime.now().strftime("%H: %M: %S")
                    print(strTime[:-2])
                    speak(f"Sir, The time is {strTime}")
                elif 'brightness' in query:
                    speak("Changing Screen Brightness")
                    s = ''
                    for i in query:
                        if i.isnumeric():
                            s+=i
                    sbc.set_brightness(s)
                elif 'from windows open' in query:
                    query = query.replace("from windows open", "")
                    speak(f"Opening {query}")
                    pg.hotkey('win')
                    time.sleep(2)
                    pg.typewrite(query, interval = 0.5)
                    pg.hotkey('enter')
                elif 'click my picture' in query:
                    speak("Clicking Picture")
                    pg.hotkey('win')
                    time.sleep(2)
                    pg.typewrite("camera", interval = 0.5)
                    pg.hotkey('enter')
                    time.sleep(10)
                    speak("Please pose for your picture!")
                    for i in range(5,0,-1):
                        speak(i)
                    pg.hotkey("enter")
                    time.sleep(2)
                    pg.hotkey("tab")
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

                elif 'how are you' in query or 'sup' in query:
                    ask = ["How are you?", "How about you?", "'sup with you?"]
                    speak(f"I am good! {random.choice(ask)}")
                    ans = takeCommand().lower()
                    if 'good' in ans or 'fine' in ans or 'great' in ans:
                        speak("That's great sir!!")
                    elif 'sad' in ans or "not good" in ans:
                        speak("What happened sir?")
                        ans_2 = takeCommand()
                        if 'nothing much' in ans_2 or 'leave it' in ans_2 or "don't want to discuss" in ans_2:
                            speak("Ok!")
                        else:
                            speak("Oh! Don't worry! Everything will be okay!")
                    
                    elif 'okay' in ans or 'ok' in ans:
                        speak("Let me make you happier!")
                        speak("You may wish to listen to some songs!")
                        music_dir = "C:\\Users\\Bhavnoor Singh\\Desktop\\Bhavnoor Singh\\Sample Music _2"
                        songs = os.listdir(music_dir)
                        # print(songs)
                        os.startfile(os.path.join(music_dir, songs[random.choice(range(0, len(songs)))]))







                elif "what's up" in query:
                    ask = ["How are you?", "How about you?", "'sup with you?"]
                    speak(f"Ceiling but yeah, I am good! {random.choice(ask)}")
                    ans = takeCommand().lower()
                    if 'good' in ans or 'fine' in ans or 'great' in ans:
                        speak("That's great sir!!")
                    elif 'sad' in ans or "not good" in ans:
                        speak("What happened sir?")
                        ans_2 = takeCommand()
                        if 'nothing much' in ans_2 or 'leave it' in ans_2 or "don't want to discuss" in ans_2:
                            speak("Ok!")
                        else:
                            speak("Oh! Don't worry! Everything will be okay!")
                    
                    elif 'okay' in ans or 'ok' in ans:
                        speak("Let me make you happier!")
                        speak("You may wish to listen to some songs!")
                        music_dir = "C:\\Users\\Bhavnoor Singh\\Desktop\\Bhavnoor Singh\\Sample Music _2"
                        songs = os.listdir(music_dir)
                        # print(songs)
                        os.startfile(os.path.join(music_dir, songs[random.choice(range(0, len(songs)))]))

                elif 'send message to' in query:
                    query1 = query.split()
                    del query1[:3]
                    rcp = None
                    for i in query1:
                        if i in whatsapp_contacts:
                            rcp = i
                    if rcp == None:
                        speak("Couldn't find any recipent")
                        continue
                    else:
                        speak(f"Sending message to {rcp}. What should I say?")
                    msg = takeCommand().lower()
                    # del query1[:query1.index("say") + 1]
                    msg_final = '%20'.join(msg.split())
                    wb.open(f"https://wa.me/{whatsapp_contacts[rcp]}?text={msg_final}")
                    time.sleep(10)
                    speak("Sending Message")
                    pg.hotkey("enter")
                    speak("message sent")
                elif 'switch tabs' in query:
                    pg.keyDown('ctrl')
                    pg.press('tab')
                    pg.keyUp('ctrl')
                elif 'switch windows' in query:
                    pg.keyDown('alt')
                    pg.press('tab')
                    pg.press('tab')
                    pg.keyUp('alt')

                elif 'type' in query:
                    query = " ".join(query.split()[1:])
                    pg.typewrite(query)
                elif 'alexa sleep' in query:
                    speak('Sleeping...')
                    while True:
                        wake_comm = takeCommand().lower()
                        if 'alexa wake up' in wake_comm:
                            speak("Hi there! I'm back!")
                            break
                        else:
                            time.sleep(1)
                
                elif ('alexa' in query and x == 1) or ('jarvis' in query and x == 0):
                    replies = ["I'm there...","Yes?","Looks like someone called me!","Here I am!!"]
                    speak(random.choice(replies))
                elif 'shutdown' in query:
                    os.system('shutdown /s /t 1')
                elif 'restart' in query:
                    os.system('shutdown /r /t 1')
                
                else:
                    file = open("not_replied.txt","a")
                    if query.strip() != 'none':
                        file.write("\n"+query)
                        file.close()
                    else:
                        file.close()
                        continue

                    
                # elif 'say' in query:
                #     query_1 = query.split()
                #     query_1.remove("say")
                #     query__final = str(' '.join(query_1))
                #     speak(query__final)
                # else:
                #     speak("Could you please repeat that again?")
                #     speak("I am not sure I understand")

                # elif "what is" in query:
                #     query1 = query.split()
                #     query1.remove("what")
                #     query1.remove("is")
                #     query_lang = query1[-1]
                #     try:
                #         del query1[query1.index("called"):]
                #     except:
                #         del query1[query1.index("in"):]
                #     translator = googletrans.Translator()
                #     result = translator.translate(str(' '.join(query1)), dest=googletrans.LANGCODES.get(query_lang))
                #     speak("It is called" + result)

                # elif "set timer" in query:
                #     query_timer = query.split()
                #     del query_timer[:query_timer.index("for") + 1]
                #     timer()
                #     if query_timer[1] == "hours" or query_timer[1] == "hour":
                #         pg.click(960,980)
                #         pg.typewrite(int(query_timer[0]))
                #     elif query_timer[1] == "minutes" or query_timer[1] == "minute":
                #         pg.click(960,980)
                #         pg.typewrite(int(query_timer[0]))
                #     elif query_timer[1] == "seconds" or query_timer[1] == "second":
                #         pg.click(960,980)
                #         pg.typewrite(int(query_timer[0]))
                #     else:
                #         pg.click(960,980)
                #         pg.typewrite(0)
                #     try:
                #         if query_timer[3] == "hours" or query_timer[3] == "hour":
                #             pg.click(960, 980)
                #             pg.typewrite(int(query_timer[2]))
                #         elif query_timer[3] == "minutes" or query_timer[3] == "minute":
                #             pg.click(960, 980)
                #             pg.typewrite(int(query_timer[2]))
                #         elif query_timer[3] == "seconds" or query_timer[3] == "second":
                #             pg.click(960, 980)
                #             pg.typewrite(int(query_timer[2]))
                #         else:
                #             pg.click(960, 980)
                #             pg.typewrite(0)
                #     except:
                #         pass
                #
                #     try:
                #         if query_timer[5] == "hours" or query_timer[5] == "hour":
                #             pg.click(960, 980)
                #             pg.typewrite(int(query_timer[4]))
                #         elif query_timer[5] == "minutes" or query_timer[5] == "minute":
                #             pg.click(960, 980)
                #             pg.typewrite(int(query_timer[4]))
                #         elif query_timer[5] == "seconds" or query_timer[5] == "second":
                #             pg.click(960, 980)
                #             pg.typewrite(int(query_timer[4]))
                #         else:
                #             pg.click(960, 980)
                #             pg.typewrite(0)
                #     except:
                #         pass
                """
                elif 'join vmc class' in query or 'vidya mandir class join' in query or 'vidyamandir class join' in query:
                    speak("Joining VMC Class")
                    wb.open('http://online.vidyamandir.com/liveclass/list')
                    time.sleep(10)
                    pg.press('tab', presses=13)
                    time.sleep(1)
                    pg.hotkey('enter')
                    time.sleep(5)
                    pg.press('tab', presses=2)
                    pg.hotkey('enter')
                    time.sleep(10)
                    pg.typewrite('singh.bhavnoor.4854@gmail.com')
                    pg.hotkey('enter')"""
