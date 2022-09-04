from unittest.mock import patch

import pytest

import models


class TestSpeech:
    def test_speech(self):
        with patch("pyttsx3.init") as _mock:
            for boolean in (True, False):
                speech = models.speech.Speech(boolean)
                speech.speak("test")
                assert speech
