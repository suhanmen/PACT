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
    n = len(xs)
    assert n % 2 == 0 and xs[-1] != 0, "Invalid input. Only even-length list with non-zero last coefficient is allowed."

    for i in range(n-1):
        if xs[i] == 0:
            continue
        else:
            # Use Newton-Raphson method to find the zero point
            x0 = 0.0
            f = lambda x: poly(xs, x)
            fp = lambda x: poly([i * xs[i] for i in range(1, n)], x)
            while True:
                x1 = x0 - f(x0) / fp(x0)
                if abs(x1 - x0) < 0.000001:
                    return x1
                else:
                    x0 = x1
