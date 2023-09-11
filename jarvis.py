import pyttsx3
import SpeechRecognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import time
import requests
import operator
from bs4 import BeautifulSoup
import pywikihow
from pywikihow import search_wikihow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui import Ui_MainWindow
import speedtest
import bs4
import features
import calendar
from keyboard import press
from keyboard import press_and_release
from keyboard import write
import keyboard
import winsound
import PyPDF2
import self

















engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()




def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak("Good morning sir")
    elif hour>12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("I am jarvis your assistant please tell me how can i help you")






def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=be7b07becbb24e22829aba73c5b67d08'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")





def pdf_reader():
    book = open('result.pdf','rb')  # not working do in some time in adobe
    pdfReader = PyPDF2.pdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total number of pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number here: "))
    page = pdfReader.getpage(pg)
    text = page.extractText()
    speak(text)

def YoutubeAuto():
    speak(f"sir, what is your command?")
    comm = self.takecommand()

    if "pause" in comm:
        keyboard.press('space bar')

    elif "unpause" in comm:
        keyboard.press('space bar')
   

    elif "restart" in comm:
        keyboard.press('0') 

    elif "mute" in comm:
        keyboard.press('m')

    elif "skip" in comm:
        keyboard.press('l')

    elif "back" in comm:
        keyboard.press('j')              

    elif "full screen" in comm:
        keyboard.press('f')

    elif "film mode" in comm:
        keyboard.press('t')         

    speak(f"done sir")    

def ChromeAuto():
    speak(f"chrome automation started")        

    command = self.takecommand()

    if "close this tab" in command:
        keyboard.press_and_release('ctrl + w')

    elif "open new tab" in command:
        keyboard.press_and_release('ctrl + t')

    elif "open new window" in command:
        keyboard.press_and_release('ctrl + n')

    elif "history" in command:
        keyboard.press_and_release('ctrl + h')







        




class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()    

    def run(self):
        self.TaskExecution()



    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.....")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("say that again please...")
            return "none"
        return query
        


    def TaskExecution(self):
     wish()
     #if 1:
     while True:
        

        self.query = self.takecommand()

        #logic building for tasks

        if "open Notepad" in self.query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        
        

        elif "open command prompt" in self.query:
            os.system("start cmd")

        elif "open camera" in self.query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k ==27:
                    break;
            cap.release()
            cv2.destroyAllWindows() #press escape to close camera

        elif "volume up" in self.query:
            pyautogui.press("volumeup")
            speak("sir volume is set up")

        elif "volume down" in self.query:
            pyautogui.press("volumedown")
            speak("sir volume is set down")

        elif "mute" in self.query:
            pyautogui.press("volumemute")
            speak("volume is muted")


        elif "IP address" in self.query:
            ip = get('https://api.ipify.org').text
            speak(f"sir your ip address is {ip}")

        elif "Wikipedia" in self.query:
            speak("searching wikipedia sir....") #say wikipedia on
            self.query = self.query.replace("wikipedia", "")
            results = wikipedia.summary(self.query, sentences=2)
            speak("sir according to wikipedia")
            speak(results)
            #print(results)

        elif "YouTube" in self.query:
            webbrowser.open("www.youtube.com")

        elif "open vit result" in self.query:
            webbrowser.open("https://admissionresults.vit.ac.in/viteee/")

        
        elif "play song" in self.query:
            kit.playonyt("Dragon Ball Super - Ultra Instinct Mastered (Clash of Gods) Piano Toccata") #give name of song here

        elif "hi" in self.query or "hello" in self.query:
            speak("Hello sir")
            continue
            
        elif "how are you" in self.query:
            speak("i am good sir what about you")
            while True:
                hi = self.takecommand()
                if "good" or "fine" in self.query:
                    speak("Happy to hear sir")
                    break

        elif "home location" in self.query:
            speak(f"ok, sir wait getting you home location")
            webbrowser.open('https://www.google.com/maps/place/Crescent+Apartments/@28.5919078,77.032638,17z/data=!3m1!4b1!4m5!3m4!1s0x390d1ac798a5bc95:0xcd1a0a2742510882!8m2!3d28.5919567!4d77.0348776')
    
        elif "map" in self.query:
            speak(f"wait sir, opening maps")
            webbrowser.open('https://www.google.com/maps/@28.5835264,77.0637824,13z')   
        

        elif "open Google" in self.query: #used if you want to display the data only
            speak("sir, what should i search for you on google")
            cm = self.takecommand()
            webbrowser.open(f"{cm}")

        elif "timer" in self.query or "stopwatch" in self.query:
            speak("for how many minutes sir")
            timing = self.takecommand()
            timing = timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f"I will remind you in {timing} seconds")

            time.sleep(timing)
            speak(f"Your time has finished sir")    

        elif "Chrome" in self.query:
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

        elif "Google search" in self.query: #used if u want to make jarvis speak
            import wikipedia as googleScrap
            self.query = self.query.replace("jarvis", "")
            self.query = self.query.replace("Google search", "")
            self.query = self.query.replace("Google", "")
            speak(f"sir, This is what i found on web")

            try:
                kit.search(self.query)
                result = googleScrap.summary(self.query, 3)
                speak(result)

            except:
                speak(f"No speakable Data available")   

        elif "activate security camera"  in self.query:
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                ret, frame1 = cam.read()
                ret, frame2 = cam.read()
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
                for c in contours:
                    if cv2.contourArea(c) < 5000:
                        continue
                    x, y, w, h = cv2.boundingRect(c)
                    cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('Security Cam', frame1)

        elif "Facebook" in self.query:
            speak(f"ok sir opening facebook")
            webbrowser.open("www.facebook.com")        


                

            
        
         

        

        

          
                

          

        
                    
        elif "temperature" in self.query:
         search = "temperature in delhi"
         url = f"https://www.google.com/search?q={search}"
         r = requests.get(url)
         data = BeautifulSoup(r.text, "html.parser")
         temp = data.find("div", class_="BNeawe").text
         speak(f"current {search} is {temp}")

        

        #elif "how to do mode" in query:
            #speak("how to do mode is activated please tell me what you want to know")
            #how = takecommand()
            #max_results = 1
            #how_to = search_wikihow(how, max_results)
            #assert len(how_to) == 1
            #how_to[0].print()
            #speak(how_to[0].summary)

        elif "how to do mode" in self.query:
            speak("how to do mode is activated")
            while True:
                speak("please tell me what you want to know")
                how = self.takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am unable to find this")


        elif "how much power left" in self.query or "battery" in self.query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                speak("we should charge our battery sir")
            elif percentage<=15 and percentage<=30:
                speak("we don't have enough power to work, kindly connect to the charger")
            elif percentage<=15:
                speak("we have very low power, please connect to the charger or the system will shutdown soon")
    

        elif "pause" in self.query:
         keyboard.press('space bar')

        elif "unpause" in self.query:
            keyboard.press('space bar') 

        elif "restart" in self.query:
         keyboard.press('0') 

        elif "mute" in self.query:
          keyboard.press('m')

        elif "skip" in self.query:
          keyboard.press('l')

        elif "back" in self.query:
          keyboard.press('j')              

        elif "full screen" in self.query:
           keyboard.press('f')

        elif "film mode" in self.query:
          keyboard.press('t') 

        elif "youtube tools" in self.query:
            YoutubeAuto()  

        elif "close this tab" in self.query:
          keyboard.press_and_release('ctrl + w')

        elif "open new tab" in self.query:
           keyboard.press_and_release('ctrl + t')

        elif "open new window" in self.query:
            keyboard.press_and_release('ctrl + n')

        elif "history" in self.query:
            keyboard.press_and_release('ctrl +h')

        elif "chrome automation" in self.query:
            ChromeAuto()    
               
        








            
            

            

        

            



            


           

























        elif "you can sleep now" in self.query:
            speak("okay, sir i am sleeping for now you can call me anytime i would be waiting sir.")
            sys.exit()


        elif "close notepad" in self.query:
            speak("okay sir closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "alarm" in self.query:
            speak("sir please tell me the time to set the alarm for example, set the alarm for 5:30 am")
            tt = self.takecommand()
            tt = tt.replace("set alarm to ",  "")
            tt = tt.replace(".","")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)

          




        elif "tell me a joke" in self.query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in self.query:
            os.system("shutdown /s /t 5")

        elif "sleep the system" in self.query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")    

        elif"restart the system" in self.query:
            os.system("shutdown /r /t 5")

        elif 'switch window' in self.query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me the news" in self.query:
            speak("please wait sir, fetching news for you")
            news()


        elif "where i am" in self.query or "what is my current location" in self.query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir,due to network issue i am unable to find where we are")
                pass

        elif "Instagram profile" in self.query or "profile on instagram" in self.query:
            speak("sir please enter username correctly")
            name = input("enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")

        elif "take a screenshot" in self.query or "take screenshot" in self.query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("sir please hold for a few seconds i am taking the screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot has been saved to the main folder.now i am ready for the next command")

        elif "time" in self.query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif "date today" in self.query:
            datetoday = datetime.date.today()
            speak(f"sir, the today's date is {datetoday}")

        elif "weather" in self.query:
             api_address = "https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
             speak(f"sir, write the  name of the place you want me to check the weather of")
             city = input("Enter city:")
             url = api_address + city

             json_data = requests.get(url).json()
             formatted_data = json_data['weather'] [0] ['description']
             speak(f"sir the weather of {city} is {formatted_data}")

        elif "describe yourself" in self.query:
            speak(f"sir, i was desighned by Sarthak in the month of june 2021 i am an AI model which can do mostly any task you desire sir") 


        elif "converter" in self.query:
            speak(f"sir, please enter the units you want to convert")
            num1 = input('Enter the value: ')
            unit1 = input('Which unit do you want it converted from:  ')
            unit2 = input('Which unit do you want it converted to: ')

            if unit1 == "cm" and unit2 == "m":
                ans = float(num1)/100
                speak(f"the converted unit is: {ans}")
            elif unit1 == "mm" and unit2 == "cm":
                ans = float(num1)/10
                speak(f"the converted unit is: {ans}")
               
            elif unit1 == "m" and unit2 == "cm":
                ans = float(num1)*100
                speak(f"the converted unit is: {ans}")
            elif unit1 == "cm" and unit2 == "mm":
                ans = float(num1)*10
                speak(f"the converted unit is: {ans}")
            elif unit1 == "mm" and unit2 == "m":
                ans = float(num1)/1000
                speak(f"the converted unit is: {ans}")
            elif unit1 == "m" and unit2 == "mm":
                ans = float(num1)*1000
                speak(f"the converted unit is: {ans}")
            elif unit1 == "km" and unit2 == "m":
                ans = float(num1)*1000
                speak(f"the converted unit is: {ans}")
            elif unit1 == "m" and unit2 == "km":
                ans = float(num1)/1000
                speak(f"the converted unit is: {ans}")
            elif unit1 == "mm" and unit2 == "km":
                ans = float(num1)/1000000
                speak(f"the converted unit is: {ans}")
            elif unit1 == "ft" and unit2 == "cm":
                ans = float(num1)*30.48
                speak(f"the converted unit is: {ans}")
            elif unit1 == "ft" and unit2 == "mm":
                ans = float(num1)*304.8
                speak(f"the converted unit is: {ans}")
            elif unit1 == "ft" and unit2 == "inch":
                ans = float(num1)*12
                speak(f"the converted unit is: {ans}")
            elif unit1 == "inch" and unit2 == "cm":
                ans = float(num1)*2.54
                speak(f"the converted unit is: {ans}")
            elif unit1 == "inch" and unit2 == "mm":
                ans = float(num1)*25.4 
                speak(f"the converted unit is: {ans}")    


        elif "activate calculator" in self.query:
            def add(a, b):
             return a + b
            # This function performs subtraction
            def subtract(a, b):
             return a - b
            # This function performs multiplication
            def multiply(a, b):
             return a * b
            # This function performs division
            def divide(a, b):
             return a / b
            speak(f"Select an operation.")
            speak(f"+(add)")
            speak(f"-(subtract)")
            speak(f"*(multiply)")
            speak(f"/(divide)")
            # User input
            choice = input("Enter operator to use:")
            A = int(input("Enter first number: "))
            B = int(input("Enter second number: "))
            if choice == '+':
              print(A,"+",B,"=", add(A,B))
              speak(f"The addition is: {add(A,B)}")
            elif choice == '-':
              print(A,"-",B,"=", subtract(A,B))
              speak(f"The subtraction is:{subtract(A,B)} ")
            elif choice == '*':
             print(A,"*",B,"=", multiply(A,B))
             speak(f"The multiplication is: {multiply(A,B)} ")
            elif choice == '/':
              print(A,"/",B,"=", divide(A,B))
              speak(f"The division is:{divide(A,B)} ")
            else:
             print("Invalid input")

        









             
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../BeneficialThoroughAgama-max-1mb.gif")    
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())