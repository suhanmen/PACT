# CANNOT PARSE CODE SNIPPET
def is_prime(n: int) -> bool:
    """
    is_prime returns True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    a, b = 1, 1
    count = 0
    while count < n:
        a, b = b, a + b
        if is_prime(a):
            count += 1
    return a
