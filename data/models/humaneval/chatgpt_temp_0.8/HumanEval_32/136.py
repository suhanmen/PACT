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
        raise ValueError("The length of the coefficients list should be even.")
    n = len(xs) // 2
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient should be non-zero.")
    # We know that the polynomial with even number of coefficients
    # has a solution when the largest non-zero coefficient is non-zero.
    # Using the rational root theorem we know that any root of the polynomial
    # is of the form p/q where p is a factor of the constant term and q is the
    # factor of the largest non-zero coefficient.
    # As the polynomial has at most n roots, we can iterate over all the possible
    # values of p and q to find the roots.
    roots = []
    for p in range(1, abs(xs[0])+1):
        if xs[0] % p != 0:
            continue
        for q in range(1, abs(xs[-1])+1):
            if xs[-1] % q != 0:
                continue
            x = p/q
            if abs(poly(xs, x)) < 1e-6:
                roots.append(x)
    if len
