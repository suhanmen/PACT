# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    """
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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib1 = 2
        fib2 = 3
        count = 2
        while count < n:
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
            if is_prime(fib3):
                count += 1
        return fib3
