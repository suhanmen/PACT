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
        raise ValueError("xs must have even number of coefficients")
    if xs[-1] == 0:
        raise ValueError("largest non-zero coefficient must be non-zero")
        
    # Find the range for the binary search
    max_coeff = max(abs(coeff) for coeff in xs)
    range_start = -max_coeff - 1
    range_end = max_coeff + 1
    
    # Binary search
    while range_end - range_start > 1e-10:
        mid = (range_start + range_end) / 2
        if poly(xs, mid) > 0:
            range_end = mid
        else:
            range_start = mid
            
    return range_start
