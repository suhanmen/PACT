import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and the largest non-zero coefficient guaranteed to exist. """
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient in xs must be non-zero.")
    if len(xs) % 2 != 0:
        raise ValueError("xs must have an even number of coefficients.")
    if len(xs) == 2:
        return -xs[0] / xs[1]
    else:
        # find the derivative of the polynomial
        derivative = [xs[i] * (len(xs) - i - 1) for i in range(len(xs) - 1)]
        # find a zero point of the derivative to use as an initial guess
        guess = find_zero(derivative)
        # improve the guess using Newton's method
        x = guess
        while abs(poly(xs, x)) > 1e-12:
            x -= poly(xs, x) / poly(derivative, x)
        return x
