"""
Python implementation of stack data structure and 2 use cases.

(1) reverse string
(2) balanced parentheses

Practice question from "Problem Solving with Algorithms and Data
    Structures using Python (Chapter 4.5 - 4.7)"
"""


class Stack:
    """
    Implement stack data structure using Python list
    """

    def __init__(self):  # construct an empty stack
        self.items = []

    def isEmpty(self):  # check the stack is empty
        return self.items == []

    def push(self, item):  # add a new item to the top of the stack
        self.items.append(item)

    def pop(self):  # remove the top item from the stack
        return self.items.pop()

    def peek(self):  # return the top item from the stack but does not remove it
        return self.items[len(self.items) - 1]

    def size(self):  # return the number of items on the stack
        return len(self.items)


# Use case 1: reverse string utilizing stack
def revstring(mystr):
    s = Stack()
    revstr = ""

    # push each character to the stack
    for c in mystr:
        s.push(c)

    # then remove character from the top of the stack one at a time
    while not s.isEmpty():
        revstr += s.pop()

    return revstr


# Use case 2: check if parentheses are balanced
# (1) Simple case:
#       assume the input string only has "(" or ")", no space
def checkPar_smiple(symbolStr):
    s = Stack()

    for c in symbolStr:
        if c == "(":
            s.push(c)
        else:
            if s.isEmpty():
                return False
            else:
                s.pop()

    if not s.isEmpty():
        return False
    else:
        return True


# (2) General case:
#       allowed parentheses types: ( ) [ ] { }
def checkPar(symbolStr):
    s = Stack()

    for c in symbolStr:
        if c in "{[(":
            s.push(c)
        elif c in "}])":
            if s.isEmpty():
                return False
            else:
                if not match(s.peek(), c):
                    return False
                s.pop()

    if not s.isEmpty():
        return False
    else:
        return True


# helper function
def match(open, close):
    """
    Check if the close parenthesis matches open parenthesis
    """
    opens = "{[("
    closers = "}])"
    return opens.index(open) == closers.index(close)


"""
Testing
"""


def test_revstring():
    assert revstring("apple") == "elppa"
    assert revstring("x") == "x"
    assert revstring("1234567890") == "0987654321"


def test_checkPar_simple():
    assert checkPar_smiple("((()))")
    assert not checkPar_smiple("(()")


def test_checkPar():
    assert checkPar("{({([][])}())}")
    assert not checkPar("[{()]")
