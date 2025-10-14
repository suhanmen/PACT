# CANNOT PARSE CODE SNIPPET
import math


def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
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
        raise ValueError("xs must have even number of coefficients")
    if xs[-1] == 0:
        raise ValueError("largest non zero coefficient must be non zero")
    n = len(xs) // 2
    a = xs[0:n]
    b = xs[n:]
    # find x such that poly(x) = 0 by solving ax^2 + bx + c = 0
    c = [a[i] * b[j] for i in range(n) for j in range(n)]
    return (-b[0] + math.sqrt(b[0]**2 - 4 * a[0] * c[0])) / (2 * a[0])
