import requests

class Slack:

    def __init__(self, token: str, channel_name: str):
        self.token = token
        self.channel_name = channel_name
        self.base_query = r"https://slack.com/api/chat.postMessage?token={0}&channel=%23{1}&text={{0}}&pretty=1".format(self.token, self.channel_name)

    def present_entry(self, entry: str):
        requests.post(self.base_query.format(entry))