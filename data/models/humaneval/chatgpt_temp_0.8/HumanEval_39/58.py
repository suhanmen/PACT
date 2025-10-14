# CANNOT PARSE CODE SNIPPET
def is_prime(n: int) -> bool:
    """
    is_prime checks if a number is prime or not.
    """
    if n < 2:
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
    fib = [1, 2]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    for num in fib:
        if is_prime(num):
            return num
    return None
