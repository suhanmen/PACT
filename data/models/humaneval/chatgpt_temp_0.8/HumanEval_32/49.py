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
    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("xs must have even number of coefficients and largest non zero coefficient")

    a = xs[0::2]
    b = xs[1::2]

    c = [b[0] / a[0]]
    d = [0]

    for i in range(1, len(a)):
        alpha = -a[i] * c[i - 1]
        beta = a[i] * d[i - 1] - b[i] * c[i - 1]
        gamma = b[i] * d[i - 1]

        c.append(beta / alpha)
        d.append(gamma / alpha)

    n = len(a) - 1
    z = -d[n] / c[n]

    for k in range(n - 1, -1, -1):
        z = (-d[k] - a[k + 1] * z) / c[k]

    return z
