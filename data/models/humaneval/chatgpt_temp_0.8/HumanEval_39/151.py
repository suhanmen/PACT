# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
    """
    is_prime checks whether a number is prime or not.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 3
    count = 2
    prev = 2
    curr = 3
    while count < n:
        prev, curr = curr, prev + curr
        if is_prime(curr):
            count += 1
    return curr
