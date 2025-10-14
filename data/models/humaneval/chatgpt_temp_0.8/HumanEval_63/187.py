# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    """Efficiently compute the n-th element of the fibfib number sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for i in range(3, n+1):
            fibfib_n = a + b + c
            a, b, c = b, c, fibfib_n
        return fibfib_n
