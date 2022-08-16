"""The Game Module"""
from datetime import datetime


class Game:
    """A game object"""

    def __init__(self):
        """initialize the game"""
        self.turn = 1
        self.running = True

    def next_turn(self):
        """Advance the turn of the game"""
        self.turn += 1

    def end_game(self, character, story):
        """End the game session and save the output"""
        print(f"You ended the game at level: {character.level}")
        print(f"Here is your story")
        print("*" * 88)
        with open(
            f"stories/{character.name}s_{story.style}_{story.genre}_story_{datetime.now().isoformat()}.txt",
            "w",
        ) as new_story:
            new_story.write(
                f"A {story.genre} yet {story.style} story about {character.name}: \n"
            )
            for line in story.history:
                new_story.write("")
                new_story.write(f"{line} \n")
                new_story.write("")
                print(line)
            print("*" * 88)
            new_story.write(f"The game ended on turn {self.turn}. \n")
            new_story.write(
                f"{character.name}'s experience totaled {character.experience} at level {int(character.level)}"
            )
