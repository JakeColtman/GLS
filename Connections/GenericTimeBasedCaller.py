
from time import time, sleep
from datetime import datetime, timedelta
import requests


class GenericTimeBasedCaller:
    def __init__(self, get_messages_function):
        self.last_checked = time()
        self.tick_period_seconds = 20
        self.seen_messages = []
        self.get_messages_function = get_messages_function

    def get_messages(self):
        while True:
            current_time = datetime.now()
            sleep(self.tick_period_seconds)
            start_time = current_time + timedelta(minutes=-10)
            resp = self.get_messages_function()
            self.last_checked = current_time
            print("tick")
            self.seen_messages = list(filter(lambda x: x > datetime.now() + timedelta(minutes=-30), self.seen_messages))
            yield [x for x in resp["messages"] if datetime.fromtimestamp(float(x["ts"])) not in self.seen_messages]

    def set_tick_period(self, seconds):
        self.tick_period_seconds = seconds

    def start(self):
        for message_list in self.get_messages():
            print(message_list)
            for message in message_list:
                self.seen_messages.append(datetime.fromtimestamp(float(message["ts"])))
                yield message["text"]
