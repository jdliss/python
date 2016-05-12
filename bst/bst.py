class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class BST:
    def __init__(self):
        self.root = None

    def __init__(self, *params):
        if type(params) is Node:
            root = params
        elif type(params[0]) is str and type(params[1]) is int:
            root = Node(params[0], params[1])

