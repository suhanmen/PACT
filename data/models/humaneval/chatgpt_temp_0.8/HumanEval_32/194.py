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
        raise ValueError("The list of coefficients must have an even number of elements")
    n = len(xs) - 1
    if xs[n] == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero")
    a = xs[n-1] / xs[n]
    b = xs[n-2] / xs[n]
    c = -xs[n-1] / xs[n] * a - xs[n-3] / xs[n]
    d = -xs[n-2] / xs[n] * a
    p = (3*c - math.pow(b, 2)) / 3
    q = (2*math.pow(b, 3) - 9*b*c + 27*d) / 27
    delta = math.pow(q/2, 2) + math.pow(p/3, 3)
    if delta > 0:
        u = math.pow((-q/2 + math.sqrt(delta)), 1/3)
        v = math.pow((-q/2 - math.sqrt(delta)), 1/3)
        return round((u + v - b/3*a), 2)
    elif delta == 0:
        u = math.pow((-q/2), 1/3)
        return round(2*u - b/3*a, 2)
    else:
        u = math.pow(math.sqrt(-p/3), 2)
        v = math.atan2(math.sqrt(-delta), -q/2)
        return round(2*u*math.cos(v/3) - b/3*a, 2)
