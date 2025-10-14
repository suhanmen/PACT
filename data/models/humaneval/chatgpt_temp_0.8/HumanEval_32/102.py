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
    assert len(xs) % 2 == 0, "The input list should have even number of coefficients"
    assert xs[-1] != 0, "The largest non-zero coefficient of the input polynomial should not be zero"
    
    # Initial values for the search range
    lower_bound, upper_bound = -10.0, 10.0
    tolerance = 1e-8
    
    while True:
        # Check if the search range is too small
        if upper_bound - lower_bound < tolerance:
            return (lower_bound + upper_bound) / 2
        
        # Find the midpoint of the sear
