"""
Python implementation of queue data structure and several use cases.

Practice question from "Problem Solving with Algorithms and Data
    Structures using Python (Chapter 4.12 - 4.14)"
"""


import random


class Queue:
    """
    Implement queue data structure using Python list
    """

    def __init__(self):   # construct an empty queue
        self.items = []

    def isEmpty(self):  # check if the queue is empty
        return self.items == []

    def enqueue(self, item):  # add a new item to the rear of the stack
        self.items.insert(0, item)  # will be O(n)

    def dequeue(self):  # remove the front item from the queue
        return self.items.pop()  # will be O(1)

    def size(self):  # return the number of items in the queue
        return len(self.items)


# Use case 1: Simulate hot potato game
def play_hotpotato(nameList, num):
    simqueue = Queue()

    for name in nameList:  # initialize the queue
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        # dequeue 1 person at a time after going through "num" people
        simqueue.dequeue()

    # return the last person remain in the queue
    return simqueue.dequeue()


# Use case 2: Simulate printing tasks
class Printer:
    def __init__(self, pagesPerMinute):
        self.pagerate = pagesPerMinute
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        # Assume length of each print task ranges from 1 to 20, equally likely
        self.pages = random.randrange(1, 11)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def newPrintTask(numStudent):
    # Assume each student print twice.
    # Average frequency (in sec) of one task been created
    freq = (60 * 30) // numStudent
    num = random.randrange(1, freq + 1)
    # if the randomly generated number is 180, a new task is created
    if num == freq:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute, numStudent):
    printer = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask(numStudent):  # if new task will be created
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not printer.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            printer.startNext(nexttask)
        printer.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


# Simulate 1-hour printing tasks 10 times.
# Assume: 5 pages per minute; 20 students
for i in range(10):
    simulation(3600, 5, 20)


"""
Tests
"""


def test_play_hotpotato():
    assert play_hotpotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7) == "Susan"
