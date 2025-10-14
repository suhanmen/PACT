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
        raise ValueError("The list of coefficients should have an even number of elements.")
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient should be non-zero.")
    for i in range(len(xs)):
        xs[i] /= xs[-1]
    xs = xs[:-1]
    n = len(xs) // 2
    roots = [complex(*z) for z in zip(xs[::2], xs[1::2])]
    while len(roots) < n:
        roots.append(0)
    f = lambda x: poly(xs, x)
    fprime = lambda x: sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs)])
    for i in range(n):
        root = roots[i]
        for _ in range(10):
            root -= f(root) / fprime(root)
        roots[i] = root
    return roots[0].real
