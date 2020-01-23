import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

# print(voices[1].id)
MASTER="master"
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ! " + MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon ! "+ MASTER)
    else:
        speak("Good Evening !"+ MASTER)

    speak(" your assistant at service. Please tell me how may i help you ?")

def sendEmail(to ,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail("pradeep.ramola@somaiya.edu",to,content)
    server.close()
def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-US')
        print(f"You said: {query}\n")
        audio= r.listen(source,timeout=1,phrase_time_limit=10)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        # query=None 
    return query              

wishMe()
query=takeCommand()
# print(query)
if 'wikipedia' in query.lower():
    speak("Searching wikipedia...")  
    query=query.replace("wikipedia","")  
    result =wikipedia.summary(query, sentences =2) 
    print(result)
    speak(result)  
elif 'open youtube' in query.lower():
    speak("Opening youtube as quickly as possible..")
    chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chromedir).open("youtube.com")
    # webbrowser.open("youtube.com")

elif 'open google' in query.lower():
    speak("Opening google as quickly as possible..")
    chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chromedir).open("google.com")    

elif 'open github' in query.lower():
    speak("Opening heroku as quickly as possible..")
    chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chromedir).open("github.com")


elif 'open heroku' in query.lower():
    speak("Opening github as quickly as possible..")
    chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chromedir).open("https://dashboard.heroku.com/apps")        

elif 'open reddit' in query.lower():
    speak("Opening reddit as quickly as possible..")
    chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chromedir).open("reddit.com")

# elif 'open photos' in query.lower():
#     photos= os.listdir("C:\\Users\\pradeep\\Pictures")
#     print(photos)
    
#     os.startfile(os.path.join(photos[3][1]))

elif " time " in query.lower():
    strtime=datetime.datetime.now().strftime("%H : %M : %S")
    print(strtime)
    speak("time is"+strtime)

elif 'open visual studio code' in query.lower():
    codepath="E:\\Microsoft VS Code\\Code.exe"
    speak("Okay master")
    os.startfile(codepath)

elif " send mail" in query.lower():
    try:
        speak("what should i send")
        content =takeCommand()
        print("content")
        to="pradeep.ramola@somaiya.edu"
        sendEmail(to,content)
    except Exception as e:
        print(e) 


elif 'google information' in query.lower():
    speak("google information as quickly as possible..")
    query=query.replace("google information on","")
    chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chromedir).open("google.com//?query="+query)        


