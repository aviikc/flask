#encoding = utf-8
import json
import random

class QuoteMaker:
    def __init__(self):
        with open("app\quotes.json", "r") as json_file:
            self.quotes = json.load(json_file)

    def random_quote(self):
        return self.quotes[random.randint(0, len(self.quotes)-1)]
