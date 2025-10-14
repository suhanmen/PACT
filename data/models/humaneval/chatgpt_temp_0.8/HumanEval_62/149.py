def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # Initialize an empty list to hold the coefficients of the derivative polynomial
    derivative_coeffs = []
    # Loop through the coefficients of the original polynomial, ignoring the constant term
    for i in range(1, len(xs)):
        # Calculate the derivative of the term with respect to x
        derivative_term = xs[i] * i
        # Append the derivative term to the list of coefficients for the derivative polynomial
        derivative_coeffs.append(derivative_term)
    # Return the list of coefficients for the derivative polynomial
    return derivative_coeffs
