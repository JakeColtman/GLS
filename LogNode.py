from multiprocessing.connection import Listener


class LogNode:
    def __init__(self, node_id: int):
        self.node_id = node_id

    def start(self):
        address = ('localhost', 6000)
        listener = Listener(address)
        conn = listener.accept()
        while True:
            msg = conn.recv()
            print(msg)
