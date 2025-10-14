def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list for the derivative coefficients
    derivative_xs = []
    # Iterate through the coefficients, starting from the second one
    for i in range(1, len(xs)):
        # Calculate the derivative coefficient
        derivative_coefficient = xs[i] * i
        # Add the derivative coefficient to the list
        derivative_xs.append(derivative_coefficient)
    # Return the derivative coefficients
    return derivative_xs
