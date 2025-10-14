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
        raise ValueError("list of coefficients must have even length")
    if xs[-1] == 0:
        raise ValueError("largest non-zero coefficient must be non-zero")
    for i in range(len(xs) - 1, -1, -1):
        if xs[i] != 0:
            break
    deg = i
    if deg == 0:
        return float("inf")
    x = -xs[deg-1]/xs[deg]
    for i in range(100):
        fx = poly(xs, x)
        if math.isclose(fx, 0):
            return x
        dfdx = sum([i*xs[i]*math.pow(x, i-1) for i in range(1, deg+1)])
        x -= fx/dfdx
    return x
