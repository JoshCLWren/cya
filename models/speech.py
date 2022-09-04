import pyttsx3


class Speech:
    def __init__(self, speech_decision):
        self.engine = pyttsx3.init()
        self.speech_decision = speech_decision

    def speak(self, text):
        print(text)
        if self.speech_decision:
            self.engine.say(text)
            self.engine.runAndWait()
