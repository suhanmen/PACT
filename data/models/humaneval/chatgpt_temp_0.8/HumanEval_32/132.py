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
        raise ValueError("List xs must have even number of coefficients")
    max_coeff = max(xs)
    if max_coeff == 0:
        raise ValueError("List xs must contain a non-zero coefficient")
    for i in range(len(xs)):
        xs[i] /= max_coeff
    for i in range(len(xs)):
        if xs[i] == 0:
            xs[i] = 1e-10
    n = len(xs) // 2
    a = [xs[2 * i] for i in range(n)]
    b = [xs[2 * i + 1] for i in range(n)]
    c = [0] * n
    d = [0] * n
    c[0] = -b[0] / a[0]
    d[0] = -a[n - 1] / b[n - 1]
    for i in range(1, n):
        c[i] = -b[i] / (a[i] + c[i - 1] * b[i - 1])
        d[i] = (d[i - 1] * b[i - 1] - a[n - i - 1]) / (a[n - i - 1] * c[i - 1] - b[i - 1])
    x = (d[n - 1] * c[n - 2] - a[n - 1]) / (b[n - 1] + d[n - 1] * a[n - 2])
    return x
