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


class TestGame:
    def test_game(self):
        game = models.game.Game()
        game.next_turn()
        assert game.turn == 2
        assert game.running
        char = models.character.Character("test")
        speech = models.speech.Speech(False)
        story = models.story.Story(
            char.name,
            speech,
        )
        game.end_game(char, story)
