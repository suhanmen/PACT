def derivative(xs: list):
    """
    Calculate the derivative of a polynomial represented by its coefficients.
    """
    n = len(xs)
    if n == 1:
        return [0]
    else:
        return [xs[i]*i for i in range(1, n)]
