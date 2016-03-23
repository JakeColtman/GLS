from LogNode import LogNode
from PresentationNode import PresentationNode
from Connections.Presentation.Slack import Slack
from LogFile import LogFile
from LogNode import LogNode

from Repository import Repository

FILE_NAME = "logs.csv"

logs = LogFile(FILE_NAME)
slack_presenter = Slack("", "logtest")
presentation_node = PresentationNode(logs, slack_presenter)

log_node = LogNode(1, logs)

try:
    log_node.start()
except KeyboardInterrupt:
    print("game over")
    print("game over")
    #Repository().store_node(presentation_node, "presentation_node.pickle")
