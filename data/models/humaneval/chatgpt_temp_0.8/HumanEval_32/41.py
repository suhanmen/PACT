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
    assert len(xs) % 2 == 0, "xs must have even number of coefficients"
    n = len(xs) - 1
    assert xs[n] != 0, "largest coefficient must be non zero"
    a = xs[n - 1] / xs[n]
    b = xs[n - 2] / xs[n]
    c = a * a - xs[n - 2] / xs[n - 1]
    x1 = (-a - math.sqrt(c)) if c >= 0 else None
    x2 = (-a + math.sqrt(c)) if c >= 0 else None
    x3 = -1 / b if b != 0 else None
    candidates = [x for x in [x1, x2, x3] if x is not None]
    return poly(xs, candidates[0]) if candidates else None
