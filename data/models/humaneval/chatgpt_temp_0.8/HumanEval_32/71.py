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
        return None # return None if xs is not even or largest coefficient is 0
    
    # we know that the polynomial has an even degree, so we can find its root by bisection
    left, right = -1, 1
    while poly(xs, left) * poly(xs, right) > 0:
        left -= 1
        right += 1
    mid = (left + right) / 2
    while abs(poly(xs, mid)) > 1e-6:
        if poly(xs, mid) * poly(xs, left) < 0:
            right = mid
        else:
            left = mid
        mid = (left + right) / 2
    return mid
