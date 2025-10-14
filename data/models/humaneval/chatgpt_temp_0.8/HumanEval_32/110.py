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
        raise ValueError("List must have even number of coefficients.")
    max_coeff = max(xs)
    if max_coeff == 0:
        raise ValueError("Polynomial must have at least one non-zero coefficient.")
    n = len(xs) - 1
    if n % 2 != 0:
        raise ValueError("Polynomial must have an even degree.")
    a = xs[0]
    b = xs[1]
    c = xs[2]
    d = xs[3]
    p = (3 * a * c - b**2) / (3 * a**2)
    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)
    discriminant = q**2 / 4 + p**3 / 27
    if discriminant >= 0:
        u = (-q / 2 + math.sqrt(discriminant))**(1/3)
        if u == 0:
            x1 = -b / (3 * a)
            return x1
        else:
            v = -p / (3 * u * a)
            x1 = u + v - b / (3 * a)
            return x1
    else:
        u = math.sqrt(-p / 3)
        v = math.acos(-(q / (2 * math.sqrt(-p**3 / 27))))
        x1 = 2 * u * math.cos(v / 3) - b / (3 * a)
        return x1
