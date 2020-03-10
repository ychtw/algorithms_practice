"""
Python implementation of linked list (unordered list) 
    data structure and several use cases.

Practice question from "Problem Solving with Algorithms and Data
    Structures using Python (Chapter 4.21)"
"""


class Node:
    """
    Each node object must hold at least two pieces of information.
        - First, the node must contain the list item itself.
            We will call this the data field of the node.
        - In addition, each node must hold a reference to the next node.
    """
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        new = Node(item)
        # change the "next" ref of the new node to refer to the old 1st node of the list
        new.setNext(self.head)
        # modify the head of the list to refer to the new node
        self.head = new

    def size(self) -> int:
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item) -> bool:
        current = self.head
        while current is not None:
            if current.getData == item:
                return True
            else:
                current = current.getNext()
        return False  # traverse through the list, but not found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        # traverse the list and find the item to be removed
        while not found:
            if current.getData == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # reconstruct the link relationship
        if previous is not None:
            # if the item to be removed is the 1st item of the list
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        new = Node(item)
        current = self.head
        previous = None

        if self.size() == 0:
            new.setNext(self.head)
            self.head = new
        else:
            # traverse through the list to the end
            while current is not None:
                previous = current
                current = current.getNext()
            previous.setNext(new)

    def index(self, item):
        current = self.head
        count = 0
        while current.getData() != item:
            count += 1
            current = current.getNext()
        return count

    def insert(self, position, item):
        new = Node(item)
        current = self.head
        previous = None
        count = 0
        
        while count < position:
            previous = current
            current = current.getNext()
            count += 1

        previous.setNext(new)
        new.setNext(current)

    def pop(self):
        current = self.head
        previous = None

        # traverse through the list to the end
        while current.getNext() is not None:
            previous = current
            current = current.getNext()

        previous.setNext(current.getNext())
        return current
