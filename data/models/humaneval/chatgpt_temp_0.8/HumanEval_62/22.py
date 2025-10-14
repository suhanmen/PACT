def derivative(xs: list):
    """Return the derivative of a polynomial represented by the given coefficients."""
    return [i * xs[i] for i in range(1, len(xs))] if len(xs) > 1 else [0]
