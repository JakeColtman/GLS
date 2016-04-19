import json
import re
from Command import Command


class Parser:
    def __init__(self, config_file_location="config.json"):
        self.config = {}
        self.location = config_file_location
        self.load()

    def load(self):
        with open(self.location, 'r') as infile:
            self.config = json.load(infile)

    def save(self):
        with open(self.location, 'w') as outfile:
            json.dump(self.config, outfile)

    def add_command(self, pattern, ttype):
        self.config["commands"][pattern] = ttype
        self.save()

    def parse_message(self, message):
        print("message", message)
        for pattern in self.config["commands"]:
            compiled = re.compile(pattern)
            match = compiled.match(message)
            if match:
                return Command(self.config["commands"][pattern], [x for x in match.groups()])

if __name__ == "__main__":
    parser = Parser()
    print(parser.parse_message("add_command git_pull (git_pull)").content)
