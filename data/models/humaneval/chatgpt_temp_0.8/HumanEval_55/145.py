# CANNOT PARSE CODE SNIPPET
def fib(n: int) -> int:
    """Return n-th Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
