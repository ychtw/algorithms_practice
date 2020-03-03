"""
Practice question extracted from "Problem Solving with Algorithms and Data
    Structures using Python (Chapter 1.13)"

Description:
- Each gate has a label for identification and a single output line.
- Methods to allow a user of a gate to ask the gate for its label.
- Ability to know its output value.
"""


class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.out = self.performGateLogic()
        return self.out


class Connector:
    def __init__(self, fromgate, togate):
        self.fromgate = fromgate
        self.togate = togate
        togate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + ": "))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + ": "))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pin = None

    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.getLabel() + ": "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a + b >= 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class NandGate(AndGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        if super().performGateLogic():
            return 0
        else:
            return 1


class NorGate(OrGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        if super().performGateLogic():
            return 0
        else:
            return 1
