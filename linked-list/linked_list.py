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

    def find(self, data, currentNode=-1):
        if currentNode is -1:
            currentNode = self.head

        if currentNode.data == data:
            return currentNode
        else:
            return self.find(data, currentNode.next) if currentNode.next else None

    def find_parent(self, data, currentNode=-1):
        if currentNode is -1:
            currentNode = self.head

        if currentNode.next is not None:
            if currentNode.next.data == data:
                return currentNode
            else:
                return self.find_parent(data, currentNode.next) if currentNode.next else None

    def pop(self):
        tail = self.tail()
        self.find_parent(tail.data).next = None
        return tail

    def pop_front(self):
        head = self.head
        self.head = self.head.next
        return head

    def delete(self, data):
        if self.head.data == data:
            self.pop_front()
        else:
            self.find_parent(data).next = self.find(data).next


