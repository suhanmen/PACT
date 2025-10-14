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
    assert len(xs) % 2 == 0, "Polynomial should have even number of coefficients"
    assert xs[0] != 0, "Leading coefficient should not be zero"
    for i in range(len(xs)):
        if xs[i] != 0:
            break
    else:
        return None  # All coefficients are zero

    a0 = xs[i]
    a1 = xs[i + 1]
    a2 = xs[i + 2]
    delta = a1 * a1 - 4 * a0 * a2
    if delta < 0:
        return None  # No real solution
    elif delta == 0:
        return -a1 / (2 * a0)
    else:
        x1 = (-a1 + math.sqrt(delta)) / (2 * a0)
        x2 = (-a1 - math.sqrt(delta)) / (2 * a0)
        return x1 if x1 < x2 else x2
