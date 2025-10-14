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
        raise ValueError("The list must have an even number of coefficients.")
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero.")

    a = xs[-2] / xs[-1]
    b = xs[-3] / xs[-1]
    c = xs[-4] / xs[-1]

    q = (3*b - a**2) / 9
    r = (9*a*b - 27*c - 2*a**3) / 54
    discriminant = q**3 + r**2

    if discriminant > 0:
        s = math.copysign(1, r + math.sqrt(discriminant)) * math.pow(abs(r + math.sqrt(discriminant)), 1/3)
        t = math.copysign(1, r - math.sqrt(discriminant)) * math.pow(abs(r - math.sqrt(discriminant)), 1/3)
        x = -a/3 + s + t
        return x
    elif discriminant == 0:
        if r == 0:
            x = -a/3
            return x
        else:
            s = math.copysign(1, r) * math.pow(abs(r), 1/3)
            x = -2*s - a/3
            return x
    else:
        theta = math.acos(r / math.sqrt(-math.pow(q, 3)))
        x1 = 2 * math.sqrt(-q) * math.cos(theta/3) - a/3
        x
