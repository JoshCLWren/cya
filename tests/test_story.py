from unittest.mock import patch

import pytest

import models


@pytest.fixture(autouse=True)
def mock_ai():
    with patch("openai.Completion.create") as mock_response:
        response = {
            "choices": [
                {
                    "text": 'Opening prompt sent to the AI: Hi, my name is: test. Write the first paragraph of a '
                    'Fantasy choose your own adventure story in a Humorous tone: The AI response returned in '
                    '5.7767 seconds: \n\nYou find yourself in a dark and musty dungeon, surrounded by damp '
                    'walls and the stench of rotting flesh. You hear the sound of rats scurrying in the '
                    'distance, and the drip, drip, drip of water echoing through the dreary hall. You see a '
                    'faint light in the distance, and you walk towards it. As you get closer, you see that '
                    'the light is coming from a torch that is attached to the wall. You reach for the torch, '
                    'but just as your hand touches it, you hear a deep, guttural voice behind you say, '
                    '"Stop! If you take one step closer, I\'ll turn you into a toad!"',
                }
            ]
        }

        mock_response.return_value = response
        yield mock_response


@pytest.fixture(autouse=True)
def mock_output():
    with patch("models.speech.Speech.speak") as mock_output:
        yield mock_output


class TestStory:
    def test_story(self, mock_ai, mock_output):
        speech = models.speech.Speech(False)
        story = models.story.Story("test_name", speech)
        assert story.intro
        prompt = story.openai_query("prompt")
        assert prompt == mock_ai.return_value["choices"][0]["text"]
        next_line = story.advance_story("decision", "test_name")
        assert next_line == mock_ai.return_value["choices"][0]["text"]
        story.pending()
        assert mock_output.call_count == 5
