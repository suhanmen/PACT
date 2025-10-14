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
        raise ValueError("The list of coefficients must have an even number of elements.")
    max_coeff = max(xs)
    if max_coeff == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero.")
    for i in range(len(xs)):
        xs[i] /= max_coeff
    roots = []
    for i in range(int(len(xs) / 2)):
        a = xs[i * 2]
        b = xs[i * 2 + 1]
        c = xs[i * 2 + 2] if i * 2 + 2 < len(xs) else 0
        d = xs[i * 2 + 3] if i * 2 + 3 < len(xs) else 0
        p = -b / (3 * a)
        q = p ** 3 + (b * c - 3 * a * d) / (6 * a ** 2)
        r = c / (3 * a)
        if q >= 0:
            s = (q + math.sqrt(q ** 2 + (r - p ** 2) ** 3)) ** (1 / 3)
        else:
            s = (-q + math.sqrt(q ** 2 + (r - p ** 2) ** 3)) ** (1 / 3) * -1
        t = (q - math.sqrt(q ** 2 + (r - p ** 2) ** 3)) ** (1 / 3)
        root = round(p + s + t, 6)
        roots.append(root)
    return max(roots, key=lambda x: abs(poly(xs, x)))
