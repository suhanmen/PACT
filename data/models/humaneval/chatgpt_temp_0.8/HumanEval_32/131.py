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
    n = len(xs) // 2
    a = xs[:n+1]
    b = xs[n+1:]
    if a[-1] == 0:
        a, b = b, a
    if a[-1] == 0:
        raise ValueError("xs must have a non-zero largest coefficient")
    if b:
        a, b = b, a
    if b:
        raise ValueError("xs must have a non-zero even coefficient")
    if a[0] == 0:
        a = a[1:]
    if a[0] == 0:
        raise ValueError("xs must have a non-zero constant coefficient")
    if len(a) == 1:
        return -a[0] / a[0]

    c = [0] * (len(a) - 1)
    for i in range(len(a) - 1):
        c[i] = a[i+1] / a[0]

    result = 0
    for i in range(100):
        x = -poly(c, result)
        if abs(x) < 1e-12:
            return result
        result += x
    raise ValueError("Unable to converge to a solution")
