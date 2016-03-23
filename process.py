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
args = parser.parse_args()

if args.node_file is not None:
    node = Repository().load_node(args.node_file)
    try:
        node.start()
    except KeyboardInterrupt:
        Repository().store_node(node, "presentation_node.pickle")
