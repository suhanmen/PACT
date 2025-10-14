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
    and largest non zero coefficient as it guarantees a solution."""
    if len(xs) % 2 != 0:
        raise ValueError("List must have even number of coefficients.")
    max_coeff = max(xs)
    if max_coeff == 0:
        raise ValueError("Cannot determine zero point for all zero coefficients.")
    else:
        degree = xs.index(max_coeff)
        xs_normalized = [coeff / max_coeff for coeff in xs]
        xs_reversed = xs_normalized[::-1]
        xs_reversed[degree] -= 1
        x_initial = 0.5
        x_next = poly(xs_reversed, x_initial) / degree
        while abs(x_next - x_initial) > 1e-8:
            x_initial = x_next
            x_next = poly(xs_reversed, x_initial) / degree
        return x_next
