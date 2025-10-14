def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Create an empty list to store the derivative coefficients
    derivative_coeffs = []
    
    # Loop through the coefficients starting from the second coefficient
    for i in range(1, len(xs)):
        # Calculate the derivative of each term using the power rule
        derivative_term = xs[i] * i
        # Add the derivative term to the list of derivative coefficients
        derivative_coeffs.append(derivative_term)
    
    # Return the list of derivative coefficients
    return derivative_coeffs
