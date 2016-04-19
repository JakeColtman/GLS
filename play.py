from Connections.Telegram import TelegramStream
from Connections.Slack import SlackOutput
from Nodes import JunctionNode

stream = TelegramStream()
output = SlackOutput()
node = JunctionNode(stream, output)
node.start()
