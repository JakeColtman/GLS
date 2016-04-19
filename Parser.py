import json
import re
from Command import Command


class Parser:
    def __init__(self, config_file_location="config.json"):
        self.config = {}
        self.location = config_file_location
        self.load()

    def load(self):
        self.config = json.load(open(self.location, 'r'))

    def save(self):
        json.dump(open(self.location, 'w'))

    def parse_message(self, message):
        print("message", message)
        for condition in self.config["commands"]:
            compiled = re.compile(condition)
            match = compiled.match(message)
            print(match)
            if match:
                return Command(self.config["commands"][condition], match.group(1))