def find_zero(xs: list):
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even length.")
    if xs[-1] == 0:
        raise ValueError("The largest coefficient must be non-zero.")
    # Find the derivative of the polynomial
    d_xs = [i * x for i, x in enumerate(xs)][1:]
    # Initial guess for Newton's method
    x0 = 1.0
    # Maximum number of iterations
    max_iter = 100
    # Tolerance for convergence
    tol = 1e-6
    # Apply Newton's method to find the zero of the polynomial
    for i in range(max_iter):
        fx = poly(xs, x0)
        dfx = poly(d_xs, x0)
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise ValueError("Newton's method did not converge.")
