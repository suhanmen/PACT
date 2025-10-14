# CANNOT PARSE CODE SNIPPET
def is_prime(n: int) -> bool:
    """
    is_prime returns True if n is prime, otherwise False.
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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        i = 3
        fib1, fib2 = 2, 3
        while True:
            fib = fib1 + fib2
            if is_prime(fib):
                i += 1
                if i == n:
                    return fib
            fib1, fib2 = fib2, fib
