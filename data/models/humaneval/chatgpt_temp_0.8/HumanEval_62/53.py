def derivative(xs: list):
    """Return the derivative of a polynomial with coefficients given by xs."""
    n = len(xs)
    if n <= 1:
        return []
    else:
        return [i * xs[i] for i in range(1, n)]
