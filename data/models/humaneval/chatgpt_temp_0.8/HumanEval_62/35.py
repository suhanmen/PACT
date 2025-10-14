python
def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list to hold the derivative coefficients
    derivative_xs = []

    # Iterate over the coefficients of the polynomial
    for i in range(1, len(xs)):
        # Compute the derivative coefficient for the current power of x
        derivative_coeff = xs[i] * i
        # Append this coefficient to the list of derivative coefficients
        derivative_xs.append(derivative_coeff)

    # Return the list of derivative coefficients
    return derivative_xs
