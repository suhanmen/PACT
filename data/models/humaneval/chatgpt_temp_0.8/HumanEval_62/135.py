def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

    degree = len(xs) - 1  # get the degree of the polynomial
    if degree == 0:  # if the degree is 0, the derivative is zero
        return [0]

    # iterate over the coefficients and calculate the derivative
    deriv = [xs[i] * i for i in range(1, degree+1)]
    return deriv
