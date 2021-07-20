import pyttsx3

tts = pyttsx3.init()

def speak(text):
    tts.say(text)
    tts.runAndWait()

def save_file(text, filename):
    tts.save_to_file(text, filename)
    tts.runAndWait()