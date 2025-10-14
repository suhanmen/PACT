# CANNOT PARSE CODE SNIPPET
def fib(n: int) -> int:
    """Return n-th Fibonacci number."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(2, n):
            a, b = b, a + b
        return b
