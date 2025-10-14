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
    dxs = []
    # Loop through the coefficients of the polynomial
    for i in range(1, len(xs)):
        # Compute the derivative of each term and append it to the result
        dxs.append(xs[i] * i)
    # Return the derivative coefficients
    return dxs
