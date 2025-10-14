import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    if xs[-1] == 0:
        raise ValueError("largest non-zero coefficient must be non-zero")
    # find the range in which the zero point exists
    a = xs[-1]
    b = -xs[-2]
    for i in range(len(xs) - 3, -1, -1):
        a, b = xs[i] + a * b, -b
    # apply bisection method to find the zero point
    if poly(xs, a) == 0:
        return a
    if poly(xs, b) == 0:
        return b
    while b - a > 1e-10:
        c = (a + b) / 2
        if poly(xs, c) == 0:
            return c
        if poly(xs, a) * poly(xs, c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
