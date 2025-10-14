def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # initialize an empty list to store the derivative coefficients
    derivative_coeffs = []
    
    # iterate through the input coefficients and calculate the derivative coefficients
    for i in range(1, len(xs)):
        derivative_coeffs.append(xs[i] * i)
    
    # return the list of derivative coefficients
    return derivative_coeffs
