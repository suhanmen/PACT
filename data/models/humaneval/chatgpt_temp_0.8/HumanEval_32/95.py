def find_zero(xs: list):
    assert len(xs) % 2 == 0, "Input list must have even number of coefficients"
    assert xs[-1] != 0, "Largest coefficient must be non-zero"

    n = len(xs) - 1
    a = xs[n-2] / xs[n]
    b = xs[n-1] / xs[n]
    c = xs[n-1] / xs[n]
    d = xs[n] / xs[n]

    for i in range(1, n-1, 2):
        a = a * b - xs[n-i-1] / xs[n]
        b = b * c - xs[n-i] / xs[n]
        c = c * d - xs[n-i+1] / xs[n]
        d = d * xs[n] / xs[n]

    delta = b**2 - 4*a*c
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)

    return x1 if abs(poly(xs, x1)) < abs(poly(xs, x2)) else x2
