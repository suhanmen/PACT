# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
    """
    is_prime checks whether the given number is prime or not.
    """
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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        count = 2
        num1, num2 = 2, 3
        while count < n:
            fib = num1 + num2
            num1, num2 = num2, fib
            if is_prime(fib):
                count += 1
        return fib
