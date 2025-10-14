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
        return None
    a = xs[-1]
    b = xs[-2]
    c = xs[-3]
    d = xs[-4]
    # using cubic equation formula to solve for roots 
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    discriminant = q ** 2 + 4 * p ** 3 / 27
    if discriminant >= 0:
        w = (-q + math.sqrt(discriminant)) / 2
        if w >= 0:
            z = -math.pow(w, 1 / 3)
        else:
            z = math.pow(-w, 1 / 3)
        u = -p / (3 * a)
        x1 = z + u
        return x1
    else:
        radius = math.sqrt(-p / 3)
        angle = math.acos(-math.sqrt(-27 / p ** 3) * q / 2)
        x1 = 2 * radius * math.cos(angle / 3) - b / (3 * a)
        return x1
