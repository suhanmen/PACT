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
    if len(xs) % 2 != 0 or xs[-1] == 0:
        raise ValueError("Input list must have even number of coefficients and a non-zero highest coefficient")
    degree = len(xs) - 1
    if degree == 2:
        a, b, c = xs[0], xs[1], xs[2]
        if b * b - 4 * a * c < 0:
            raise ValueError("Equation has no real roots")
        return (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    else:
        # Use Newton-Raphson method to find a zero of the polynomial
        # Initial guess is the midpoint of the interval [-2M, 2M], where M is the largest absolute value
        M = max([abs(coeff) for coeff in xs]) / xs[-1]
        x = 0
        for i in range(1000):
            fx = poly(xs, x)
            if abs(fx) < 1e-10:
                return x
            fpx = sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs)])
            if fpx == 0:
                raise ValueError("Derivative is zero at x={}".format(x))
            x = x - fx / fpx
        raise ValueError("Fail
