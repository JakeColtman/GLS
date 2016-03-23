from multiprocessing.connection import Listener
from LogFile import LogFile
from LogEntry import LogEntry

class LogNode:
    def __init__(self, node_id: int, log_file: LogFile):
        self.node_id = node_id
        self.log_file = log_file

        self.log_id = max([x.log_id for x in log_file.get_rows() if x.node_id == self.node_id])
        if self.log_id == None:
            self.log_id = 1

    def start(self):
        address = ('localhost', 6000)
        listener = Listener(address)
        conn = listener.accept()
        while True:
            msg = conn.recv()
            self.log_id += 1
            self.log_file.add_row(LogEntry([self.node_id, self.log_id, msg]))
