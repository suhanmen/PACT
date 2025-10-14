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
        raise ValueError("The polynomial must have an even number of coefficients.")
    max_coeff = max([abs(c) for c in xs])
    if max_coeff == 0:
        return 0
    xs = [c / max_coeff for c in xs]
    guess = 0.5
    tolerance = 1e-15
    max_iterations = 1000
    for i in range(max_iterations):
        f = poly(xs, guess)
        if abs(f) < tolerance:
            return guess * max_coeff
        df = sum([i * c * math.pow(guess, i-1) for i, c in enumerate(xs) if i > 0])
        gu
