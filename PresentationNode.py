from LogFile import LogFile

class PresentationNode:

    def __init__(self, log_file: LogFile, presenter):
        self.presenter = presenter
        self.log_file = log_file

        self.most_recent_values = {}

    def read_new_entries(self):
        lines = self.log_file.get_rows()
        for line in lines:
            if line.node_id not in self.most_recent_values:
                self.most_recent_values[line.node_id] = 0
            if line.log_id > self.most_recent_values[line.node_id]:
                self.presenter.present_entry(line.message)
                self.most_recent_values[line.node_id] = line.log_id
