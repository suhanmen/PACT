# CANNOT PARSE CODE SNIPPET
def fibfib(n: int) -> int:
    """
    The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b, c = 1, 1, 0
        for i in range(3, n+1):
            d = a + b + c
            c = b
            b = a
            a = d
        return d - b - c
