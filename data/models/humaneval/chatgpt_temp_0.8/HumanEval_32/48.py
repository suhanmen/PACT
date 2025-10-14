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
        raise ValueError("Polynomial must have even number of coefficients.")
    max_coeff = max(xs)
    if max_coeff == 0:
        raise ValueError("Polynomial must have non-zero coefficients.")
    for i in range(len(xs)):
        xs[i] /= max_coeff
    roots = []
    for i in range(len(xs) - 1):
        if xs[i] == 0:
            continue
        for j in range(i + 1, len(xs)):
            if xs[j] == 0:
                continue
            a = xs[i]
            b = xs[j]
            c = sum([xs[k] for k in range(len(xs)) if k != i and k != j])
            p = (b + c) / a
            q = (b - c) / a
            discriminant = p * p - 4 * q
            if discriminant < 0:
                continue
            root1 = (-p + math.sqrt(discriminant)) / 2
            root2 = (-p - math.sqrt(discriminant)) / 2
            if root1 == root2:
                roots.append(root1)
            else:
                roots.append(root1)
                roots.append(root
