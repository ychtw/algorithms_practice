"""
Convert decimal numbers to use base other than 10.

Allowed base ranges: 2 ~ 16

For example:
- binary number (base 2)
- octal number (base 8)
- hexadecimal number (base 16)

"""
from stack import Stack


def convertBase(num: int, base: int) -> str:
    rem_stack = Stack()
    digits = "0123456789ABCDEF"
    result = ""

    while num > 0:
        rem_stack.push(num % base)  # push remainder to stack
        num = num // base

    # construct the converted value by removing remainders from the stack
    while not rem_stack.isEmpty():
        result += digits[rem_stack.pop()]

    return result


"""
Test
"""


def test_convertBase():
    assert convertBase(42, 2) == "101010"
    assert convertBase(25, 8) == "31"
    assert convertBase(25, 16) == "19"
    assert convertBase(256, 16) == "100"
    assert convertBase(233, 16) == "E9"
