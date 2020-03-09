"""
Convert infix math expression into postfix form.
    Assumptions:
    - The infix expression is a string of tokens delimited by spaces.
    - The operator tokens are *, /, +, -, ( and ).
    - The operand tokens are either:
        - single-character identifiers A, B, C, and so on
        - integers

Evaluate math expression in postfix form.
    Assumptions:
    - Operands are integers.

Practice question from "Problem Solving with Algorithms and Data
    Structures using Python (Chapter 4.9)"
"""
from stack import Stack
import string

letters = string.ascii_letters


def infix_to_postfix(infixExpr: str) -> str:
    # operator precedence
    prec = {"**": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfix_list = []

    # Convert the input infix string to a list by using the string method split
    infix_list = infixExpr.split()

    for token in infix_list:
        # if token in letters or token in "0123456789":
        if token in letters or is_int(token):
            postfix_list.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            while opStack.peek() != "(":
                postfix_list.append(opStack.pop())
            # if the top item of opStack is "(", simply remove it
            opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfix_list.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfix_list.append(opStack.pop())

    return " ".join(postfix_list)


def eval_postfix(postfixExpr: str):
    operands = Stack()

    # Convert the input infix string to a list by using the string method split
    postfix_list = postfixExpr.split()

    for token in postfix_list:
        if is_int(token):
            operands.push(int(token))
        else:  # if the token is an operator: +, -, *, /
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = do_math(token, operand1, operand2)
            operands.push(result)

    return operands.pop()


def is_int(expr: str) -> bool:
    try:
        num = int(expr)
    except ValueError:
        return False
    return True


def do_math(operator: str, operand1: int, operand2: int):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2


"""
Tests
"""


def test_infix_to_postfix():
    assert infix_to_postfix("A * B + C * D") == "A B * C D * +"
    assert (
        infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )")
        == "A B + C * D E - F G + * -"
    )
    assert infix_to_postfix("( A + B ) * ( C + D )") == "A B + C D + *"
    assert infix_to_postfix("( A + B ) * C") == "A B + C *"
    assert infix_to_postfix("A + B * C") == "A B C * +"
    assert infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )") == "10 3 5 * 16 4 - / +"
    assert infix_to_postfix("5 * 3 ** ( 4 - 2 )") == "5 3 4 2 - ** *"


def test_eval_postfix():
    assert eval_postfix("7 8 + 3 2 + /") == 3.0
    assert eval_postfix("3 2 * 4 5 * +") == 26
    assert eval_postfix("17 10 + 3 * 9 /") == 9.0
