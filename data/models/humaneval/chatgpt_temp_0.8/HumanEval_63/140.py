# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # Initialize the first three elements of the sequence
        a, b, c = 0, 0, 1
        # Use a loop to compute the n-th element of the sequence
        for i in range(3, n+1):
            a, b, c = b, c, a + b + c
        return c
