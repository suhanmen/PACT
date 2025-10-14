def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list to hold the coefficients of the derivative polynomial
    derivative_coeffs = []
    # Loop through each power of x in the original polynomial
    for i in range(1, len(xs)):
        # Multiply each coefficient by its corresponding power of x to get the coefficient in the derivative polynomial
        derivative_coeffs.append(xs[i] * i)
    # Return the list of coefficients of the derivative polynomial
    return derivative_coeffs
