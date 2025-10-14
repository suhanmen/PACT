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
    derivative_xs = []
    
    # loop through the list of coefficients, starting from the second coefficient
    for i in range(1, len(xs)):
        # calculate the coefficient of the derivative term (i.e. the power of x is reduced by 1)
        derivative_coeff = xs[i] * i
        
        # add the derivative coefficient to the list
        derivative_xs.append(derivative_coeff)
        
    # return the list of derivative coefficients
    return derivative_xs
