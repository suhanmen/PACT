def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # initialize an empty list to store the result
    result = []
    # iterate through the list of coefficients.
    for i in range(1, len(xs)):
        # multiply each coefficient by its index, which is the power it is raised to.
        # append this new coefficient to the result list.
        result.append(xs[i] * i)
    return result
