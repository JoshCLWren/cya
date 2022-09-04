import pyttsx3  # pragma: no cover


class Speech:  # pragma: no cover
    def __init__(self, speech_decision):  # pragma: no cover
        self.engine = pyttsx3.init()  # pragma: no cover
        self.speech_decision = speech_decision  # pragma: no cover

    def speak(self, text):  # pragma: no cover
        print(text)  # pragma: no cover
        if self.speech_decision:  # pragma: no cover
            self.engine.say(text)  # pragma: no cover
            self.engine.runAndWait()  # pragma: no cover
