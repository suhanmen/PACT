# CANNOT PARSE CODE SNIPPET
def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        raise ValueError("n should be greater than 0")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        x = 3
        y = 5
        count = 2
        while count < n:
            z = x + y
            if is_prime(z):
                count += 1
                if count == n:
                    return z
            x = y
            y = z
        raise ValueError("n is greater than the number of prime Fibonacci numbers found")

def is_prime(num: int) -> bool:
    """
    is_prime checks whether a given integer is a prime number or not.
    """
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
