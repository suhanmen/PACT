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
    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("xs must have an even number of coefficients and a non-zero leading coefficient")

    degree = len(xs) - 1
    a = xs[-2] / xs[-1]
    b = sum(xs[:-2]) / xs[-1]
    c = xs[0] / xs[-1]

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        raise ValueError("the polynomial has no real roots")

    if discriminant == 0:
        return -b / (2 * a)

    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    if 0 <= root1 <= 1:
        return root1
    elif 0 <= root2 <= 1:
        return root2
    else:
        raise ValueError("the polynomial has no root between 0 and 1")
