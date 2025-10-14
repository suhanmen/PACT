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
    n = len(xs) - 1
    if n % 2 != 0 or xs[n] == 0:
        raise ValueError("xs should have even length and largest coefficient should not be zero")
    else:
        a = xs[n]
        b = xs[n-1]
        c = xs[0] - xs[n-2]
        d = xs[n-3]
        x0 = -b/(3*a)
        p = (3*a*c-b*b)/(3*a*a)
        q = (2*b*b*b-9*a*b*c+27*a*a*d)/(27*a*a*a)
        Delta = (q/2)**2 + (p/3)**3
        u = -q/2 + math.sqrt(Delta)
        v = -q/2 - math.sqrt(Delta)
        y0 = ((u if u>0 else v)**(1/3)) + ((-(u if u>0 else v))**(1/3))
        return round(x0+y0, 2)
