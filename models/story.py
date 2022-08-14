"""Story Model"""

import os
import time

import openai


class Story:
    """Story Class"""

    def __init__(self, name, genre="Fantasy", style="Humorous"):
        """Initialize a story"""
        self.genre = genre
        self.style = style
        self.history = []
        openai.api_key = os.getenv("api_key")
        self.intro = self.opening_prompt(genre, style, name)

    def opening_prompt(self, genre, style, name):
        """Send the Openai api a story prompt"""
        intro = f"Hi, my name is: {name}. Write the first paragraph of a {genre} choose your own adventure story in a {style} tone:"
        self.history.append(f"Opening prompt sent to the AI: {intro}")
        return self.openai_query(prompt=intro)

    def openai_query(self, prompt):
        tic = time.perf_counter()
        self.pending()
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        toc = time.perf_counter()
        result = response["choices"][0]["text"]
        self.history.append(
            f"The AI response returned in {toc - tic:0.4f} seconds: {result}"
        )
        return result

    def advance_story(self, decision, name):
        """advance the narrative"""
        prompt = (
            f"Continue my {self.genre} yet {self.style} choose your own adventure story picking up from your "
            f"last message which was: '{self.history[-1]}' I, {name}, choose to: {decision}. Now what? "
        )
        self.history.append(f"{name}'s response: {decision}")
        line = self.openai_query(prompt=prompt)
        self.history.append(line)
        return line

    @staticmethod
    def pending():
        """Output that the ai is working on a response"""
        print("*" * 88)
        print("Waiting on a response from the Artificial Intelligence...")
        print("*" * 88)
