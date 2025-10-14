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
        raise ValueError("List xs must have even number of coefficients")
    if xs[-1] == 0:
        raise ValueError("List xs must have a non-zero largest coefficient")

    n = len(xs) - 1
    if n == 1:
        # linear equation
        return -xs[0] / xs[1]
    elif n == 2:
        # quadratic equation
        a, b, c = xs
        delta = b * b - 4 * a * c
        if delta < 0:
            raise ValueError("Equation has no real roots")
        else:
            return (-b + math.sqrt(delta)) / (2 * a)
    else:
        # use Newton-Raphson method for finding roots
        # starting from initial guess x = 1
        x = 1
        while True:
            fx = poly(xs, x)
            fpx = sum([i * xs[i] * math.pow(x, i - 1) for i in range(1, n + 1)])
            x_new = x - (fx / fpx)
            if math.isclose(x, x_new):
                return x
            else:
                x = x_new
