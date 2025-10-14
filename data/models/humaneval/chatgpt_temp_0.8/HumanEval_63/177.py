# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    # Base cases
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    # Initialize variables
    a, b, c, d, e = 0, 0, 1, 1, 1
    # Loop to compute fibfib(n)
    for i in range(3, n+1):
        a, b, c, d, e = b, c, d, e, a+b+c+d
    return e
