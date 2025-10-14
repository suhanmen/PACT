# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
    """Helper function to check if a given number is prime"""
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None

    fib = [0, 1]
    i = 2

    while True:
        next_fib = fib[i - 1] + fib[i - 2]

        if is_prime(next_fib):
            if n == 1:
                return next_fib
            else:
                n -= 1

        fib.append(next_fib)
        i += 1
