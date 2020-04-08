"""
Practice question extracted from "Problem Solving with Algorithms and Data
    Structures using Python (Chapter 1.13)"

Description:
A very common example to show the details of implementing a user-defined class
    is to construct a class to implement the abstract data type Fraction.
- The operations for the Fraction type will allow a Fraction data object to
    behave like any other numeric value.
- We need to be able to add, subtract, multiply, and divide fractions.
- We also want to be able to show fractions using the standard “slash” form,
    for example 3/5.
- In addition, all fraction methods should return results in their lowest terms
    so that no matter what computation is performed, we always end up with
    the most common form.
"""


def cal_gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        if bottom == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        else:
            self.num = top
            self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        gcd = cal_gcd(newnum, newden)
        return Fraction(newnum // gcd, newden // gcd)

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        gcd = cal_gcd(newnum, newden)
        return Fraction(newnum // gcd, newden // gcd)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        gcd = cal_gcd(newnum, newden)
        return Fraction(newnum // gcd, newden // gcd)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        gcd = cal_gcd(newnum, newden)
        return Fraction(newnum // gcd, newden // gcd)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum


"""
Test cases
"""
f1 = Fraction(3, 4)
f2 = Fraction(2, 3)


def test_print(capsys):
    print(f1)
    captured = capsys.readouterr()
    assert captured.out == "3/4\n"


def test_add():
    assert f1 + f2 == Fraction(17, 12)


def test_minus():
    assert f1 - f2 == Fraction(1, 12)


def test_multiply():
    assert f1 * f2 == Fraction(1, 2)


def test_division():
    assert f1 / f2 == Fraction(9, 8)


def test_gt():
    assert f1 > f2


def test_lt():
    assert not f1 < f2
