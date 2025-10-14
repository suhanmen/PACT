# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
    """
    Returns True if the given number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    """
    if n < 1:
        raise ValueError("n should be a positive integer.")
    a, b = 1, 1
    count = 2
    while count < n:
        a, b = b, a + b
        count += 1
    while not is_prime(b):
        a, b = b, a + b
    return b
