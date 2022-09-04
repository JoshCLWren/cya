import pytest

import models


class TestCharacter:
    def test_character_creation(self):
        char = models.character.Character("test")
        assert char.name == "test"
        char.level_up(100)
        assert char.level == 1.01
