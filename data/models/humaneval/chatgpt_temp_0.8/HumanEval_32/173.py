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
        raise ValueError("The list should have an even number of coefficients")
    # Find the coefficient with the largest magnitude
    max_coeff = max([abs(coeff) for coeff in xs])
    # Divide all coefficients by the coefficient with the largest magnitude to simplify the problem
    xs = [coeff / max_coeff for coeff in xs]
    # Define a helper function to evaluate the polynomial
    def f(x):
        return poly(xs, x)
    # Define the search interval as [-2, 2]
    a, b = -2, 2
    while abs(b - a) > 1e-6:
        # Calculate the midpoint of the interval
        c = (a + b) / 2
        # Evaluate the polynomial at the midpoint
        y = f(c)
        # Determine which half of the interval to keep
        if y == 0:
            return c
        elif y < 0:
            a = c
        else:
            b = c
    # Return the midpoint of the final interval as the zero of the polynomial
    return (a + b) / 2
