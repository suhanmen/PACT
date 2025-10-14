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
        raise ValueError("The number of coefficients must be even.")
    max_coeff = max([abs(coeff) for coeff in xs])
    if max_coeff == 0:
        raise ValueError("All coefficients are zero.")
    xs = [coeff / max_coeff for coeff in xs]  # normalize coefficients

    def f(x):
        return poly(xs, x)

    def f_prime(x):
        n = len(xs) - 1
        return sum([(i+1) * xs[i+1] * math.pow(x, i) for i in range(n)])

    x0 = 1.0  # initial guess for the zero point
    eps = 1e-6  # tolerance for convergence
    max_iter = 1000  # maximum number of iterations
    for i in range(max_iter):
        fx = f(x0)
        fpx = f_prime(x0)
        if abs(fx) < eps:
            return x0  # found a zero point
        if abs(fpx) < eps:
            raise ValueError("Derivative is zero at x = {}".format(x0))
        x0 = x0 - fx / fpx
    raise ValueError("Failed to converge after {} iterations".format(max_iter))
