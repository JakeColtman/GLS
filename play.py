from Connections.Telegram import TelegramStream
from Connections.Slack import SlackOutput
from Nodes import JunctionNode, ConsumerNode
from Parser import Parser

stream = TelegramStream()
output = SlackOutput()
node = ConsumerNode(stream, parser = Parser())
node.start()
