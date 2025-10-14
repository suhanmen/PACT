def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) <= 1:
        # The derivative of a polynomial of degree <= 0 is 0.
        return [0]
    else:
        # Compute the derivative by multiplying each coefficient with its degree.
        return [xs[i] * i for i in range(1, len(xs))]
