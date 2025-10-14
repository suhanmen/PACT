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
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even length.")
    n = len(xs) - 1
    if xs[n] == 0:
        raise ValueError("The largest coefficient must not be zero.")
    # Use Newton's method to find a zero
    x = 1.0 # Starting point
    while abs(poly(xs, x)) > 1e-10:
        # Compute the derivative of the polynomial
        deriv = sum([i * xs[i] * math.pow(x, i - 1) for i in range(1, n + 1)])
        x -= poly(xs, x)/deriv
    return x
