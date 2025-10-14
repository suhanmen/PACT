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

    # Check if the length of xs is even
    if len(xs) % 2 == 1:
        raise ValueError("The list must have an even number of coefficients.")
    
    # Check if the largest non-zero coefficient is zero
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient must not be zero.")
    
    # Find the center point of the polynomial
    center = -xs[-2] / (2 * xs[-1])
    
    # Evaluate the polynomial at the center point
    center_value = poly(xs, center)
    
    # Check if the center point is already a zero point
    if center_value == 0:
        return center
    
    # Check if the center point is a local maximum or minimum
    if xs[-1] > 0 and center_value > 0:
        return None
    if xs[-1] < 0 and center_value < 0:
        return None
    
    # Find the roots of the quadratic formed by the center point
    # and the two adjacent points
    a = xs[-1]
    b = xs[-2] + xs[-1] * center
    c = xs[-3] + xs[-2] * center + xs[-1] * math.pow(center, 2)
    
