"""Character Model"""


class Character:
    """A Character object"""

    def __init__(self, name):
        """Initializes the Character class"""
        self.name = name
        self.level = 1
        self.experience = 1

    def level_up(self, xp):
        """Alter the leve of a character"""
        self.experience += xp
        self.level = self.experience / 100
