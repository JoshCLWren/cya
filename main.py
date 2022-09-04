import random

import constants
from models.character import Character
from models.game import Game
from models.speech import Speech
from models.story import Story


def start():
    game = Game()

    print("Welcome to the game!")
    print("Would you like text to speech enabled?")
    speech = input()
    speech_decision = True if "y" in speech.lower() else False
    output = Speech(speech_decision)
    output.speak(text="Hello, what is your name?")
    name = input()
    character = Character(name=name)
    output.speak(text=f"Hello {character.name}!")
    output.speak(text="Let's play a choose your own adventure game!")
    random_genre = random.choice(constants.genres)
    output.speak(text=f"Enter the genre of story you want to play or Press enter for a {random_genre} story."
    )
    genre = input()
    if len(genre) == 0:
        genre = random_genre
    random_styles = random.choice(constants.styles)
    output.speak(text=f"What is the tone of this story? Or just press enter for a {random_styles} story type."
    )
    style = input()
    if len(style) == 0:
        style = random_styles
    story = Story(name=character.name, genre=genre, style=style, speech=output)
    output.speak(text=story.intro)
    while game.running:
        game.next_turn()
        output.speak(text="What do you do next?")
        print("type X to leave the game")
        next_move = input()
        if "X" in next_move.upper():
            game.running = False
        else:
            next_line = story.advance_story(decision=next_move, name=character.name)
            print("*" * 88)
            print(f"You gained {len(next_line)} experience!{bcolors.ENDC}")
            character.level_up(len(next_line))
            print(f"You are currently level: {int(character.level)}{bcolors.ENDC}")
            print("*" * 88)
            print("")
    game.end_game(character, story)
    print("*" * 88)
    output.speak(text="Thank you for playing cya.")


start()
