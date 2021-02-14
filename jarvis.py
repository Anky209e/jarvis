import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import pyjokes
import wolframalpha
import json
import ctypes
import subprocess


print("Wecome to jarvis!\n")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")


engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning,Anky")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon,Anky")
    else:
        speak("Good Evening,Anky")
    speak("I am Jarvis!!How can i Help YOU  ?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........>>>>")
        r.pause_threshold = 1
        r.energy_threshold = 500
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognising..")
        query = r.recognize_google(audio, language='en-in')
        print('You said: ', query)
    except Exception as e:
        # print(e)
        speak("Say that again please!")
        return None
    return query


if __name__ == "__main__":
    # speak("Anky is a good boy")

    wishme()
    while True:
        speak("do you need some help?")
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia sir')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
            time.sleep(3)

        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("Youtube.com")
            time.sleep(5)
        elif 'play music' in query:
            speak("Here's the music list ,lets party")
            mus_dir = r'C:\Users\Sacred Student\Desktop\StudyTonight\songs'
            songs = os.listdir(mus_dir)
            print(songs)
            os.startfile(os.path.join(mus_dir, songs[1]))
            time.sleep(5)
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strtime}")
            time.sleep(5)
        elif'vs code' in query:
            print("opening VS Code ....")
            speak("opening VS Code ....")
            vscode_path = r"C:\Users\Sacred Student\Downloads\vs code\Microsoft VS Code\Code.exe"
            os.startfile(vscode_path)
            time.sleep(5)
        elif 'discord' in query:
            print("opening discord...")
            speak("opening discord...")
            dis_path = r"C:\Users\Sacred Student\AppData\Local\Discord\Update.exe"
            os.startfile(dis_path)
            time.sleep(5)
        elif 'amazon music' in query:
            print("Opening amazon music ....")
            speak("Opening amazon music")
            ama_path = r"C:\Users\Sacred Student\AppData\Local\Amazon Music\Amazon Music.exe"
            os.startfile(ama_path)
            time.sleep(5)

        elif 'opera' in query:

            print("opening opera mini...")
            speak("opening opera mini")
            ope_path = r"C:\Users\Sacred Student\AppData\Local\Programs\Opera\launcher.exe"
            os.startfile(ope_path)
            time.sleep(5)
        elif 'tl launcher' in query:
            print("opening TL launcher...")
            speak("opening TL launcher")
            tl_path = r"C:\Users\Sacred Student\AppData\Roaming\.minecraft\TLauncher.exe"
            os.startfile(tl_path)
            time.sleep(5)
        elif 'telegram' in query:
            print("opening telegram..")
            speak("opening telegram")
            tel_path = r"C:\Users\Sacred Student\Downloads\Telegram Desktop\Telegram.exe"
            os.startfile(tel_path)
            time.sleep(5)
        elif 'notepad' in query:
            print("opening notepad...")
            speak("opening notepad sir")
            np_path = r'C:\Windows\system32\notepad.exe'
            os.startfile(np_path)
            time.sleep(5)
        elif 'paint' in query:
            print("opening Paint ...")
            speak("opening MS paint sir")
            paint_path = r'C:\Windows\system32\mspaint.exe'
            os.startfile(paint_path)
            time.sleep(5)
        elif 'snip' in query:
            print("opening SnippingTool....")
            speak("opening SnippingTool sir")
            sni_path = r'C:\Windows\system32\SnippingTool.exe'
            os.startfile(sni_path)
            time.sleep(5)
        elif 'github' in query:
            print("opening git hub....")
            speak("opening git hub sir")
            git_path = r'"C:\Users\Sacred Student\AppData\Local\GitHubDesktop\GitHubDesktop.exe"'
            os.startfile(git_path)
            time.sleep(5)
        elif 'powershell' in query:
            print("opening powershell...")
            speak("opening powershell sir")
            pows_path = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
            os.startfile(pows_path)
            time.sleep(5)
        elif 'calculator' in query:
            print("opening calculator...")
            speak("opening calculater sir")
            cal_path = r'C:\Windows\System32\calc.exe'
            os.startfile(cal_path)
            time.sleep(5)
        elif 'task manager' in query:
            print("opening task manager....")
            speak("opening task manager sir")
            man_path = r'C:\Windows\system32\Taskmgr.exe'
            os.startfile(man_path)
            time.sleep(5)
        elif 'pdf reader' in query:
            print("opening pdf reader...")
            speak("opening pdf reader sir")
            pdf_path = r'"C:\Users\Sacred Student\AppData\Local\SumatraPDF\SumatraPDF.exe"'
            os.startfile(pdf_path)
            time.sleep(5)
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif 'search' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        # elif 'empty recycle bin' in query:
        #     winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        #     speak("Recycle Bin Recycled")
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.nl / maps / place/" + location + "")
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        

        # basic questions

        elif "who i am" in query:
            speak("If you talk then definately your human.")
        elif "why you came to world" in query:
            speak("Thanks to Anky. further It's a secret")
        elif 'is love' in query:
            speak("It is just Chamadi matter which sucks")
        elif "who are you" in query:
            speak("I am your virtual assistant created by Anky")
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Anky ")

        elif 'good bye' or 'stop':
            speak("I am going sir bye and thanks for using me see you later")
            print("Call me if you need any help")
            break

        else:
            speak("sir i cant understand your command please say again")
