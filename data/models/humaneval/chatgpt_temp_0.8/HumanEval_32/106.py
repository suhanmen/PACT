# CANNOT PARSE CODE SNIPPET
import math


def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
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
        raise ValueError("The list must have an even number of coefficients.")
    if xs[-1] == 0:
        raise ValueError("The largest non zero coefficient must be non zero.")
    # The polynomial can be written in the form (x-a)(x-b)(x-c)...(x-y)(x-z),
    # where a,b,c,...,z are the roots of the polynomial.
    # Since we know that the polynomial has an even degree, it has an even number of roots.
    # Therefore, we can pair the roots and find their average to get the zero point of the polynomial.
    roots = []
    i = 0
    while i < len(xs) - 1:
        a, b = xs[i], xs[i + 1]
        if a == 0:
            roots.append(0)
        else:
            roots.append(-b / a)
        i += 2
    return sum(roots) / len(roots)
