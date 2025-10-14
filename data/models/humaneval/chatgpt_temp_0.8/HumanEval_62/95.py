def derivative(xs: list):
    """Return the derivative of a polynomial represented by the given list of coefficients."""
    return [c * i for i, c in enumerate(xs[1:], 1)]
