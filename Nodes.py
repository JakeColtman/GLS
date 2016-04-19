class JunctionNode:
    def __init__(self, input_stream, output_stream):
        self.input_stream, self.output_stream = input_stream, output_stream


class ConsumerNode:
    def __init__(self, stream):
        self.stream = stream
