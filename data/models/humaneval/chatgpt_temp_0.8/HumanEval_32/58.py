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
        return None

    n = len(xs) // 2
    a = xs[-1]
    b = xs[-2]
    c = xs[-2:]
    d = xs[-2*n:]

    if a == 0:
        return None

    x0 = -b / (2 * a)
    p = poly(d, x0)

    if abs(p) < 1e-6:
        return x0

    if p > 0:
        return None

    delta = b**2 - 4*a*c[0]
    if delta < 0:
        return None

    x1 = (-b - math.sqrt(delta)) / (2 * a)
    p = poly(d, x1)

    if abs(p) < 1e-6:
        return x1

    x2 = (-b + math.sqrt(delta)) / (2 * a)
    p = poly(d, x2)

    if abs(p) < 1e-6:
        return x2

    return None
