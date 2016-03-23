import argparse

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

parser = argparse.ArgumentParser(description='Parse creation inputs')
parser.add_argument("--node_file", dest = "node_file")
parser.add_argument("--node_type", dest = "node_type")
parser.add_argument("--create", dest = "create")

args = parser.parse_args()

node = None
if args.create == "true":
    node = Repository().load_node(args.node_file)
else:
    logs = LogFile(FILE_NAME)
    if args.node_type == "slack":
        slack_presenter = Slack("", "logtest")
        node = PresentationNode(logs, slack_presenter)
    else:
        node = LogNode(logs)

try:
    node.start()
except KeyboardInterrupt:
    Repository().store_node(node, args.node_file)
