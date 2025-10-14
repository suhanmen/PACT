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
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution. """
    
    if len(xs) % 2 == 0 and xs[0] != 0:
        n = len(xs) - 1
        a, b = -1000, 1000
        while abs(b - a) >= 0.0001:
            c = (a + b) / 2
            if poly(xs, a) * poly(xs, c) < 0:
                b = c
            else:
                a = c
        return round(c, 2)
    else:
        return "Incorrect input."
