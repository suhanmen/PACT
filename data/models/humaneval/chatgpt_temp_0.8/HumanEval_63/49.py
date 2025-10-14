def fibfib(n: int):
    if n == 0 or n == 1: # base case
        return 0
    elif n == 2: # base case
        return 1
    else:
        # initialize variables
        a, b, c, d, e = 0, 0, 1, 1, 1
        for i in range(3, n+1):
            # update variables using the fibfib formula
            a, b, c, d, e = b, c, d, e, a+b+c+d+e
        return e
