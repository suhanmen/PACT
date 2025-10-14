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

    fib_seq = [2, 3]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    for num in fib_seq:
        if is_prime(num):
            return num
