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
    
    # initialize the first three fibfib numbers
    fibfib_prev3 = 0
    fibfib_prev2 = 1
    fibfib_prev1 = 1
    
    # compute the nth fibfib number
    for i in range(3, n+1):
        fibfib_current = fibfib_prev1 + fibfib_prev2 + fibfib_prev3
        fibfib_prev3 = fibfib_prev2
        fibfib_prev2 = fibfib_prev1
        fibfib_prev1 = fibfib_current
    
    return fibfib_current
