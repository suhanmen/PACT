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
    n = len(xs) - 1
    while xs[n] == 0:
        n -= 1
    if n % 2 != 0:
        raise ValueError("The largest non-zero coefficient must have an even degree.")
    a = xs[n]
    b = xs[n-1]
    c = xs[n-2]
    d = xs[n-3]
    p = (b/a - (c/a)**2/3)*3/2
    q = ((c/a)/3)**3 + (d/a) - (c/a)*(b/a)/3
    y1 = (-2*q/p) * math.cos(math.acos(3*p/(2*q))/3) - (c/a)/3
    y2 = (-2*q/p) * math.cos((math.acos(3*p/(2*q))/3) + 2*math.pi/3) - (c/a)/3
    y3 = (-2*q/p) * math.cos((math.acos(3*p/(2*q))/3) - 2*math.pi/3) - (c/a)/3
    return y1 if y1.imag == 0 else y2 if y2.imag == 0 else y3 if y3.imag == 0 else None
