def is_prime(n: int) -> bool:
    """
    is_prime returns True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b, count = 2, 3, 2
        while count < n:
            c = a + b
            if is_prime(c):
                count += 1
                if count == n:
                    return c
            a, b = b, c
