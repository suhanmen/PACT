# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
    """
    is_prime checks if a given number is prime.
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
        prev = 3
        curr = 5
        count = 3
        while count < n:
            next_term = prev + curr
            prev = curr
            curr = next_term
            if is_prime(curr):
                count += 1
        return curr
