import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def solve_quadratic(a, b, c):
    """
    Finds the roots of a quadratic equation of the form ax^2 + bx + c = 0.
    Returns a tuple containing the roots.
    """
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return (-b / (2 * a),)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
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
        raise ValueError("List of coefficients must have even length.")
    a = xs[-2]
    b = xs[-1]
    c = sum([coeff * math.pow(-1, i) for i, coeff in enumerate(xs[:-2])])
    if a == 0:
        return -c / b
    else:
        roots = solve_quadratic(a, b, c)
        if roots is None:
            return None
        else:
            return roots[0]
