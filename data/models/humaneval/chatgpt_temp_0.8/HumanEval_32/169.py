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
        raise ValueError("xs must have an even number of coefficients")
    highest_non_zero_coefficient = max(xs[:-1])
    if highest_non_zero_coefficient == 0:
        raise ValueError("xs must have a non-zero coefficient other than the constant term")
    # Guess initial bounds for the root
    bounds = [-abs(highest_non_zero_coefficient), abs(highest_non_zero_coefficient)]
    while True:
        # Find the midpoint of the bounds
        midpoint = sum(bounds) / 2
        # Evaluate the polynomial at the midpoint
        value = poly(xs, midpoint)
        # Check if we found a root
        if math.isclose(value, 0):
            return midpoint
        # Check which half of the bounds to keep
        if value > 0:
            bounds[1] = midpoint
        else:
            bounds[0] = midpoint
