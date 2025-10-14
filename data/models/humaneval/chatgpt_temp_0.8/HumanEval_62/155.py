def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # create an empty list to store coefficients of the derivative polynomial
    derivative_coeffs = []
    # iterate through the coefficients of the original polynomial, starting from the second coefficient
    for i in range(1, len(xs)):
        # multiply each coefficient by its corresponding power of x
        derivative_coeff = xs[i] * i
        # add the resulting coefficient to the list of derivative coefficients
        derivative_coeffs.append(derivative_coeff)
    # return the list of derivative coefficients
    return derivative_coeffs
