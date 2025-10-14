import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
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
        raise ValueError("List xs must have even number of coefficients")
    n = len(xs) // 2
    if xs[n] == 0:
        raise ValueError("Largest non zero coefficient is zero")
    a = xs[0:n]
    b = xs[n:]
    # Reverse the coefficients
    a.reverse()
    b.reverse()
    # Calculate the derivative of a and b
    da = [a[i] * (i+1) for i in range(len(a)-1)]
    db = [b[i] * (i+1) for i in range(len(b)-1)]
    # Combine the coefficients of a and b after multiplication
    c = []
  
