def fibfib(n: int):
    """
    The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 0 if n == 1 else 1
    else:
        a, b, c = 0, 0, 1
        for i in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c
