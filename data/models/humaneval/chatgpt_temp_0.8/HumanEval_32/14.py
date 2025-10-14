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
    # Check that xs has an even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients")
    
    # Find the largest non-zero coefficient
    max_coeff = max([abs(coeff) for coeff in xs])
    if max_coeff == 0:
        raise ValueError("xs must have at least one non-zero coefficient")
    
    # Find initial bounds for bisection
    left_bound = -max_coeff - 1
    right_bound = max_coeff + 1
    
    # Use bisection to find a root
    while abs(right_bound - left_bound) > 1e-10:
        midpoint = (left_bound + right_bound) / 2
        if poly(xs, midpoint) == 0:
            return midpoint
        elif poly(xs, left_bound) * poly(xs, midpoint) < 0:
            right_bound = midpoint
        else:
            left_bound = midpoint
    
    return (left_bound + right_bound) / 2
