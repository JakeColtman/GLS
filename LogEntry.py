
class LogEntry:

    def __init__(self, row):
        self.node_id, self.log_id, self.message = row
        self.node_id = int(self.node_id)
        self.log_id = int(self.log_id)