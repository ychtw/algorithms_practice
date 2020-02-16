def karatsuba(x, y):
    n = max(len(str(x)), len(str(y)))  # max number of digits between x and y

    # base case
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    # if not, calculate recursively
    else:
        # divide both x and y into 2 parts
        # note: if length is an odd number, calculation here will assure
        #       that the first half is shorter
        a = x // 10 ** (n // 2)  # first half of x
        b = x % 10 ** (n // 2)  # second half of x
        c = y // 10 ** (n // 2)  # first half of y
        d = y % 10 ** (n // 2)  # second half of y

        # (1) recursively calculate a * c
        ac = karatsuba(a, c)
        # (2) recursively calculate b * d
        bd = karatsuba(b, d)
        # (3) recursively calculate (a + b) * (c + d)
        pq = karatsuba(a + b, c + d)
        # compute (3) - (2) - (1)
        adbc = pq - ac - bd

        return (10 ** (n // 2 * 2) * ac) + (10 ** (n // 2) * adbc) + bd


# test cases
def test_even_equal_len():
    assert karatsuba(1234, 5678) == 1234 * 5678


def test_odd_equal_len():
    assert karatsuba(123, 567) == 123 * 567


def test_x_longer():
    assert karatsuba(123, 45) == 123 * 45


def test_y_longer():
    assert karatsuba(123, 4567) == 123 * 4567


def test_long():
    assert (
        karatsuba(
            3141592653589793238462643383279502884197169399375105820974944592,
            2718281828459045235360287471352662497757247093699959574966967627,
        )
        == 3141592653589793238462643383279502884197169399375105820974944592
        * 2718281828459045235360287471352662497757247093699959574966967627
    )
