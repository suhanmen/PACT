def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # We will calculate the derivative of the polynomial by multiplying
    # each coefficient by its corresponding power of x and subtracting 1
    # from the power. For example, if the polynomial is 3 + 2x + 5x^2, then
    # the derivative is 2 + 10x.
    derivative_coeffs = []
    for i in range(1, len(xs)):
        derivative_coeffs.append(i * xs[i])
    return derivative_coeffs
