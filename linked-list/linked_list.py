class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        if type(data) is Node:
            self.head = data
        else:
            self.head = Node(data)

    def append(self, data, currentNode=-1):
        node = Node(data) if type(data) is str else data

        if currentNode is -1:
            currentNode = self.head

        if currentNode.next is None:
            currentNode.next = node
        else:
            self.append(node, currentNode.next)

    def printList(self, currentNode=-1):
        if currentNode is -1:
            currentNode = self.head

        print currentNode.data
        if currentNode.next is not None:
            self.printList(currentNode.next)

    def count(self, currentNode=-1):
        if currentNode is -1:
            currentNode = self.head

        if currentNode is not None:
            if currentNode.next is not None:
                return 1 + self.count(currentNode.next)
            else:
                return 1
        else:
            return 0

    def tail(self, currentNode=-1):
        if currentNode is -1:
            currentNode = self.head
        return currentNode if not currentNode.next else self.tail(currentNode.next)

    def 


ll = LinkedList("head node")
ll.append("first node")
ll.append("second node")
ll.append("third node")
ll.append("fourth node")
ll.append("fifth node")

ll.printList()
print ll.count()
print ll.tail().data
