import pickle

class Repository:

    def store_node(self, node, file_name):
        pickle.dump(node, open(file_name, "wb"))

    def load_node(self, file_name):
        return pickle.load(open(file_name, "rb"))
