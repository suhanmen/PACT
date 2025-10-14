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
    if len(xs) % 2 == 1 or xs[-1] == 0:
        raise ValueError('xs should have an even number of coefficients and the largest non-zero coefficient')
    # The roots of a polynomial can be found by setting it to 0 and solving for x.
    # We will use the numpy module's roots function to find the roots.
    import numpy as np
    roots = np.roots(xs)
    # We will return only the real root(s), if any.
    for root in roots:
        if isinstance(root, complex) and root.imag == 0:
            return root.real
        elif not isinstance(root, complex):
            return root
