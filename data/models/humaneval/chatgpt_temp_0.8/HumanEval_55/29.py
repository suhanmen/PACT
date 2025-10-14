# CANNOT PARSE CODE SNIPPET
def fib(n: int) -> int:
    """Return the n-th Fibonacci number."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
