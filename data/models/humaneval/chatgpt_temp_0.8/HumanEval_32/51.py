def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    if xs[-1] == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero.")
    # divide by the largest non-zero coefficient to simplify calculation
    a = xs[-1]
    xs = [coeff / a for coeff in xs]
    # define the derivative of the polynomial
    def deriv(xs, x):
        return sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs)][1:])
    # use Newton's method to find the zero
    
