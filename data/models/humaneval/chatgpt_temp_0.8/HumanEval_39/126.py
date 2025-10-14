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
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 2, 3
        count = 2
        while True:
            c = a + b
            if is_prime(c):
                count += 1
            if count == n:
                return c
            a, b = b, c
