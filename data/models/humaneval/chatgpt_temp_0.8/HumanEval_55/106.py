# CANNOT PARSE CODE SNIPPET
def fib(n: int) -> int:
    """
    Return the n-th Fibonacci number.

    Args:
        n: An integer representing the position of the desired Fibonacci number.

    Returns:
        An integer representing the n-th Fibonacci number.

    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1 or n == 2:
        return 1

    prev_prev = 1
    prev = 1

    for i in range(3, n + 1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current

    return prev
