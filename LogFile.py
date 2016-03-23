
class LogFile:

    def __init__(self, file_name):
        self.file_name = file_name

    def get_rows(self):
        with open(self.file_name, "r") as fileOpen:
            lines = fileOpen.readlines()
            lines = [x.split(",") for x in lines]
            return lines