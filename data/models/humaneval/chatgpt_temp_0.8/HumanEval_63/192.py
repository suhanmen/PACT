# CANNOT PARSE CODE SNIPPET
python
def fibfib(n: int) -> int:
    """Efficiently computes the n-th element of the FibFib number sequence."""
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f1, f2, f3 = 0, 0, 1
        for i in range(3, n+1):
            f1, f2, f3 = f2, f3, f1 + f2 + f3
        return f3
