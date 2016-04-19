from time import time, sleep
from datetime import datetime, timedelta
import requests


class SlackStream:
    def __init__(self, token=None, channel="C0Y1K8J0N"):
        if token is None:
            with open("slack_token.txt", "r") as file_open:
                token = file_open.read()
        self.token, self.channel = token, channel

        self.last_checked = time()
        self.base_url = r"https://slack.com/api/channels.history?token={0}&channel={1}&oldest={{0}}&pretty=1"""
        self.base_url = self.base_url.format(self.token, self.channel)
        self.tick_period_seconds = 20
        self.triggers = []

        self.seen_messages = []

    def get_messages(self):
        while True:
            current_time = datetime.now()
            sleep(self.tick_period_seconds)
            start_time = current_time + timedelta(minutes=-10)
            resp = requests.get(self.base_url.format(start_time.timestamp())).json()
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
