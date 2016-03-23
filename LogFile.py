from typing import List
from LogEntry import LogEntry


class LogFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_rows(self) -> List[LogEntry]:
        with open(self.file_name, "r") as fileOpen:
            lines = fileOpen.readlines()
            lines = [LogEntry(x.split(",")) for x in lines[1:]]
            return lines

    def add_row(self, log_entry: LogEntry) -> bool:
        with open(self.file_name, "a") as fileOpen:
            fileOpen.writelines(["\n{0},{1},{2}".format(log_entry.node_id, log_entry.log_id, log_entry.message)])