import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os





engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<= 12:
        speak("Good Morning,Anky")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon,Anky")
    else:
        speak("Good Evening,Anky")
    speak("I am Jarvis!!How can i Help YOU sir ?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........>>>>")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)
    try:
        print("Recongnising..")
        query = r.recognize_google(audio, language='en-in')
        print('user said: ',query)
    except Exception as e:
        # print(e)
        speak("Say that again please!")
        return None
    return query
if __name__ == "__main__":
    # speak("Anky is a good boy")
    
    wishme()
    if 1:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia sir')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("Youtube.com")
        elif 'play music' in query:
            speak("Here's the music list lets party")
            mus_dir = r'C:\Users\Sacred Student\Desktop\StudyTonight\songs'
            songs = os.listdir(mus_dir)
            print(songs)
            os.startfile(os.path.join(mus_dir, songs[1]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strtime}")
        elif'vs code' in query:
            print("opening VS Code ....")
            speak("opening VS Code ....")
            vscode_path = r"C:\Users\Sacred Student\Downloads\vs code\Microsoft VS Code\Code.exe"
            os.startfile(vscode_path)
        elif 'discord' in query:
            print("opening discord...")
            speak("opening discord...")
            dis_path = r"C:\Users\Sacred Student\AppData\Local\Discord\Update.exe"
            os.startfile(dis_path)
        elif 'amazon music' in query:
            print("Opening amazon music ....")
            speak("Opening amazon music")
            ama_path = r"C:\Users\Sacred Student\AppData\Local\Amazon Music\Amazon Music.exe"
            os.startfile(ama_path)
            
        elif 'opera' in query:
            
            print("opening opera mini...")
            speak("opening opera mini")
            ope_path = r"C:\Users\Sacred Student\AppData\Local\Programs\Opera\launcher.exe"
            os.startfile(ope_path)
        elif 'tl launcher' in query:
            print("opening TL launcher...")
            speak("opening TL launcher")
            tl_path = r"C:\Users\Sacred Student\AppData\Roaming\.minecraft\TLauncher.exe"
            os.startfile(tl_path)
        elif 'telegram' in query:
            print("opening telegram..")
            speak("opening telegram")
            tel_path = r"C:\Users\Sacred Student\Downloads\Telegram Desktop\Telegram.exe"
            os.startfile(tel_path)
        elif 'notepad' in query:
            print("opening notepad...")
            speak("opening notepad sir")
            np_path = r'C:\Windows\system32\notepad.exe'
            os.startfile(np_path)
        elif 'paint' in query:
            print("opening Paint ...")
            speak("opening MS paint sir")
            paint_path = r'C:\Windows\system32\mspaint.exe'
            os.startfile(paint_path)
        elif 'snip' in query:
            print("opening SnippingTool....")
            speak("opening SnippingTool sir")
            sni_path = r'C:\Windows\system32\SnippingTool.exe'
            os.startfile(sni_path)
        elif 'github' in query:
            print("opening git hub....")
            speak("opening git hub sir")
            git_path = r'"C:\Users\Sacred Student\AppData\Local\GitHubDesktop\GitHubDesktop.exe"'
            os.startfile(git_path)
        elif 'powershell' in query:
            print("opening powershell...")
            speak("opening powershell sir")
            pows_path = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
            os.startfile(pows_path)
        elif 'calculator' in query:
            print("opening calculator...")
            speak("opening calculater sir")
            cal_path = r'C:\Windows\System32\calc.exe'
            os.startfile(cal_path)
        elif 'task manager' in query:
            print("opening task manager....")
            speak("opening task manager sir")
            man_path = r'C:\Windows\system32\Taskmgr.exe'
            os.startfile(man_path)
        elif 'pdf reader' in query:
            print("opening pdf reader...")
            speak("opening pdf reader sir")
            pdf_path = r'"C:\Users\Sacred Student\AppData\Local\SumatraPDF\SumatraPDF.exe"'
            os.startfile(pdf_path)
        else:
            speak("sir i cant understand your command please say again")


