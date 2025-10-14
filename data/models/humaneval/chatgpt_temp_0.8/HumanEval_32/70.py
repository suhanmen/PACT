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
        raise ValueError("Input list must have an even number of coefficients")
    a = max([abs(x) for x in xs[:-1]])
    if a == 0:
        raise ValueError("Largest non-zero coefficient must be non-zero")
    else:
        xs = [x / a for x in xs]
    n = len(xs) // 2
    if n == 1:
        return -xs[0] / xs[1]
    else:
        ys = [1] * (2 * n - 1)
        ys[1] = -xs[n]
        for i in range(2, 2 * n - 1):
            ys[i] = (xs[n + i - 1] - xs[n - i + 1])
        newton_xs = [0] * n
        newton_xs[0] = -xs[n] / xs[n + 1]
        for i in range(1, n):
            newton_xs[i] = newton_xs[i-1] - poly(ys, newton_xs[i-1]) / poly([xs[n-i+1]] + ys[:2*i], newton_xs[i-1])
        return newton_xs[-1] * a
