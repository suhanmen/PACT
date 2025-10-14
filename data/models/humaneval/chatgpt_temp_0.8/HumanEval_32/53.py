def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("List must have even number of coefficients.")
    if xs[-1] == 0:
        raise ValueError("Largest coefficient must be non-zero.")
    # Finding the limits of the search space
    limit1 = -xs[-2] / (2 * xs[-1])
    limit2 = (abs(xs[0]) + abs(xs[-2])) / abs(xs[-1])
    limit = max(limit1, limit2)
    # Applying the bisection method
    eps = 1e-10
    a, b = -limit, limit
    while b - a > eps:
        c = (a + b) / 2
        if poly(xs, c) == 0:
            return c
        elif poly(xs, a) * poly(xs, c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
