import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0:
        raise ValueError("Coefficients list must have an even number of elements.")
    if xs[-1] == 0:
        raise ValueError("Largest non-zero coefficient must be non-zero.")
    for i in range(len(xs) - 2, -1, -2):
        if xs[i] == 0:
            continue
        a, b, c = xs[i + 2], xs[i + 1], xs[i]
        disc = b * b - 4 * a * c
        if disc < 0:
            continue
        if disc == 0:
            return -b / (2 * a)
        root1 = (-b + math.sqrt(disc)) / (2 * a)
