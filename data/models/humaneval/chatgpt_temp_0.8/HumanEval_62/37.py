def derivative(xs: list):
    """Return derivative of polynomial represented by coefficients in xs."""
    return [xs[i] * i for i in range(1, len(xs))]
