# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        count = 2
        a, b = 2, 3
        while count < n:
            c = a + b
            if is_prime(c):
                count += 1
            a, b = b, c
        return c
