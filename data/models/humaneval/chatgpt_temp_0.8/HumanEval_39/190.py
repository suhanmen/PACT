# CANNOT PARSE CODE SNIPPET
def is_prime(n: int) -> bool:
    """
    Helper function to check if a number is prime.
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
        fib_prev = 2
        fib_curr = 3
        count = 2
        while count < n:
            fib_next = fib_prev + fib_curr
            if is_prime(fib_next):
                count += 1
                if count == n:
                    return fib_next
            fib_prev = fib_curr
            fib_curr = fib_next
