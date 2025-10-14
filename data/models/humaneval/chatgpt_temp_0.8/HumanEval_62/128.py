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
    
    # Iterate through the coefficients starting from the second one
    for i in range(1, len(xs)):
        # Multiply the current coefficient by its power
        derivative_coeff = xs[i] * i
        # Add the derivative coefficient to the list
        derivative_coeffs.append(derivative_coeff)
    
    # Return the list of derivative coefficients
    return derivative_coeffs
