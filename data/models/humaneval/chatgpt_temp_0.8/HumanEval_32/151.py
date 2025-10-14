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
        raise ValueError("Polynomial must have even number of coefficients")

    max_coeff = max(xs)
    if max_coeff == 0:
        raise ValueError("Largest non-zero coefficient must not be zero")

    # Find all possible roots
    roots = []
    for i in range(1, len(xs), 2):
        a = xs[i - 1]
        b = xs[i]
        c = xs[i + 1]
        D = b * b - 4 * a * c
        if D >= 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            roots.append(x1)
            roots.append(x2)

    # Find the real root
    for root in roots:
        if abs(poly(xs, root)) < 0.0001 and abs(root.imag) < 0.0001:
            return root.real

    raise ValueError("Could not find any real roots")
