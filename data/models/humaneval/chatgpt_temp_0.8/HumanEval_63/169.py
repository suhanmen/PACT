def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        # initialize variables with the first three values of the sequence
        a, b, c = 1, 1, 0
        # perform the sequence calculation for n-2 iterations
        for i in range(2, n):
            # update values a, b, c
            c, b, a = b, a + b + c, b
        # return the n-th element of the fibonacci sequence
        return b
