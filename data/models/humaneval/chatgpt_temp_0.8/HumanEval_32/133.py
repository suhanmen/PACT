import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    """
    if len(xs) % 2 == 1 or xs[-1] == 0:
        raise ValueError("xs must have an even number of coefficients and a non-zero highest coefficient")

    for i in range(-100, 101):
        if poly(xs, i) == 0:
            return i

    raise ValueError("no zero found in range -100 to 100")
