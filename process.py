from LogNode import LogNode
from PresentationNode import PresentationNode
from Connections.Presentation.Slack import Slack
from LogFile import LogFile

from Repository import Repository

FILE_NAME = "logs.csv"

def initialize():
    with open(FILE_NAME, "r") as fileOpen:
        lines = fileOpen.readlines()
        lines = [x.split(",") for x in lines]
        new_node_id = max([x[0] for x in lines[1:]])
        return LogNode(new_node_id)

print(initialize())

logs = LogFile(FILE_NAME)
slack_presenter = Slack("", "logtest")
presentation_node = PresentationNode(logs, slack_presenter)

try:
    presentation_node.start()
except KeyboardInterrupt:
    Repository().store_node(presentation_node, "presentation_node.pickle")
