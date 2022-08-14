import random

import constants
from models.character import Character
from models.game import Game
from models.story import Story
from models.text import bcolors


def start():
    game = Game()
    print(f"{bcolors.HEADER}What is your name?{bcolors.ENDC}")
    name = input()
    character = Character(name=name)
    print(f"Hello {character.name}!")
    print("Let's play a choose your own adventure game!")
    random_genre = random.choice(constants.genres)
    print(
        f"Enter the genre of story you want to play or Press enter for a {random_genre} story."
    )
    genre = input()
    if len(genre) == 0:
        genre = random_genre
    random_styles = random.choice(constants.styles)
    print(
        f"What is the tone of this story? Or just press enter for a {random_styles} story type."
    )
    style = input()
    if len(style) == 0:
        style = random_styles
    story = Story(name=character.name, genre=genre, style=style)
    print(story.intro)
    while game.running:
        game.next_turn()
        print(f"{bcolors.OKBLUE}What do you do next? (type X to leave the game){bcolors.ENDC}")
        next_move = input()
        if "X" in next_move.upper():
            game.running = False
        else:
            next_line = story.advance_story(decision=next_move, name=character.name)
            print("*" * 88)
            print(f"{bcolors.BOLD}{next_line}{bcolors.ENDC}")
            print(f"{bcolors.OKCYAN}You gained {len(next_line)} experience!{bcolors.ENDC}")
            character.level_up(len(next_line))
            print(f"{bcolors.BOLD}You are currently level: {int(character.level)}{bcolors.ENDC}")
            print("*" * 88)
            print("")
    game.end_game(character, story)
    print("*" * 88)
    print(f"{bcolors.FAIL}Thank you for playing cya.{bcolors.ENDC}")


start()
