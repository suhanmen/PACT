# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
    """Helper function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")
    if n == 1:
        return 2
    if n == 2:
        return 3
    
    first = 2
    second = 3
    count = 2
    
    while True:
        current = first + second
        first = second
        second = current
        count += 1
        if is_prime(current) and count == n:
            return current
