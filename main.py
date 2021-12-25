import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.getProperty("rate")
engine.setProperty("rate",rate-40)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def readlinesfromfile(textfilename):
    filehandle = open(textfilename, "r")
    lines = filehandle.readlines()
    for line in lines:
        speak(line)

readlinesfromfile("sample.txt")