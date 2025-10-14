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
    if xs[-1] == 0:
        raise ValueError("largest coefficient must be non-zero")
    # check if leading coefficient is negative or positive
    leading_coeff = xs[-1]
    if leading_coeff < 0:
        xs = [-1 * coeff for coeff in xs]
    # find a range where there must be a root, using the intermediate value theorem
    max_val = max([abs(coeff) for coeff in xs])
    lower_bound = -1 * (max_val + 1)
    upper_bound = max_val + 1
    f_lower = poly(xs, lower_bound)
    f_upper = poly(xs, upper_bound)
    while f_lower * f_upper > 0:
        lower_bound = lower_bound - (max_val + 1)
        upper_bound = upper_bound + (max_val + 1)
        f_lower = poly(xs, lower_bound)
        f_upper = poly(xs, upper_bound)
    # perform binary search within the range until finding a sufficiently small root
    while abs(lower_bound - upper_bound) > 1e-6:
        mid = (lower_bound + upper_bound) / 2
