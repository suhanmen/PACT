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
        return None
    a = xs[-1]
    if a == 0:
        return None
    b = xs[-2]/a
    c = xs[0]/a
    d = xs[1]/a
    p = (3*c - math.pow(b, 2))/3
    q = (2*math.pow(b, 3) - 9*b*c + 27*d)/27
    delta = math.pow(q/2, 2) + math.pow(p/3, 3)
    if delta > 0:
        u = math.pow(-q/2 + math.sqrt(delta), 1/3) - math.pow(q/2 + math.sqrt(delta), 1/3)
        return u - b/3
    elif delta == 0:
        u = -2*math.pow(q/2, 1/3) - b/3
        v = math.pow(q/2, 1/3) - b/3
        return u if u == v else None
    else:
        phi = math.acos(-q/2/math.sqrt(-math.pow(p/3, 3)))
        u = 2 * math.pow(-p/3, 0.5) * math.cos(phi/3) - b/3
        v = 2 * math.pow(-p/3, 0.5) * math.cos((phi + 2*math.pi)/3) - b/3
        w = 2 * math.pow(-p/3, 0.5) * math.cos((phi + 4*math.pi)/3) - b/3
        if round(poly(xs, u), 10) == 0:
            return u
        elif round(poly(xs, v), 10) == 0:
            return v
        elif round(poly(xs, w), 10) == 0:
            return 
