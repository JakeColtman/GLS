class JunctionNode:
    def __init__(self, input_stream, output):
        self.input_stream, self.output = input_stream, output

    def start(self):
        for message in self.input_stream.start():
            print("junctionmessage")
            print(message)
            self.output.post_message(message)


class ConsumerNode:
    def __init__(self, stream, parser):
        self.stream = stream
        self.parser = parser

    def start(self):
        for message in self.stream.start():
            parsed = self.parser.parse_message(message)
            print(parsed)