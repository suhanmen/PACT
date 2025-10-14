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
    max_coeff = max(xs)
    if max_coeff == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero.")
    # Find the derivative of the polynomial.
    dxs = [i * coeff for i, coeff in enumerate(xs)][1:]
    # Find the roots of the derivative.
    dzero1, dzero2 = sorted([(-1 * xs[1] + math.sqrt(xs[1]**2 - 4 * xs[0] * xs[2])) / (2 * xs[0]), (-1 * xs[1] - math.sqrt(xs[1]**2 - 4 * xs[0] * xs[2])) / (2 * xs[0])])
    # Check if there is a root between the two derivative roots.
    if poly(xs, dzero1) * poly(xs, dzero2) > 0:
        raise ValueError("The polynomial does not have a root between the two derivative roots.")
    # Use the bisection method to find the root.
    zero = (dzero1 + dzero2) / 2
    while abs(poly(xs, zero)) > 1e-9:
        if poly(xs, zero) * poly(xs, dzero1) > 0:
            dzero1 = zero
        else:
            dzero2 = zero
