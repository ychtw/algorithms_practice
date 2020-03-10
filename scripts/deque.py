"""
Python implementation of deque data structure and a use case.

Practice question from "Problem Solving with Algorithms and Data
    Structures using Python (Chapter 4.17 - 4.18)"
"""


class Deque:
    def __init__(self):  # construct an empty deque
        self.items = []

    def isEmpty(self):  # check the deque is empty
        return self.items == []

    def addRear(self, item):  # add a new item to the rear of the deque
        self.items.insert(0, item)

    def addFront(self, item):  # add a new item to the front of the deque
        self.items.append(item)

    def removeRear(self):  # remove the rear item from the deque
        return self.items.pop(0)

    def removeFront(self):  # remove the front item from the deque
        return self.items.pop()

    def size(self):  # return the number of items in the deque
        return len(self.items)


# Use case: check if a string is palindrome
def check_palindrome(aString: str) -> bool:
    chrDeque = Deque()

    # add each character to deque (from rear end)
    for c in aString:
        chrDeque.addRear(c)

    while chrDeque.size() > 1:
        front = chrDeque.removeFront()
        rear = chrDeque.removeRear()
        if front != rear:
            return False

    return True


"""
Tests
"""


def test_check_palindrome():
    assert check_palindrome("radar")
    assert not check_palindrome("lsdkjfskf")
