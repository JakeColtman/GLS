from LogNode import LogNode

FILE_NAME = "logs.csv"

def initialize():
    with open(FILE_NAME, "r") as fileOpen:
        lines = fileOpen.readlines()
        lines = [x.split(",") for x in lines]
        new_node_id = max([x[0] for x in lines[1:]])
        return LogNode(new_node_id)

print(initialize())