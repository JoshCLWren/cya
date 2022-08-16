from models.text import bcolors

import pyttsx3
class Speech:

    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text, color=None):
        if color:
            print(f"{color}{text}{bcolors.ENDC}")
        else:
            print(text)
        self.engine.say(text)
        self.engine.runAndWait()
