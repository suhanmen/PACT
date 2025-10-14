def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    
    # Initialize an empty list to store the derivative coefficients
    derivative_xs = []
    
    # Loop through the coefficients starting from the second one
    for i in range(1, len(xs)):
        # Multiply the coefficient by its corresponding power of x and append it to the derivative list
        derivative_xs.append(xs[i] * i)
    
    # Return the list of derivative coefficients
    return derivative_xs
