# CANNOT PARSE CODE SNIPPET
def is_prime(n: int) -> bool:
    """
    Returns True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        return None
    if n == 1:
        return 2
    if n == 2:
        return 3
    prev, curr = 2, 3
    count = 2
    while count < n:
        prev, curr = curr, prev + curr
        if is_prime(curr):
            count += 1
    return curr
