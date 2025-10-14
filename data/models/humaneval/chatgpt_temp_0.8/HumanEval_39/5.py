def is_prime(num: int) -> bool:
    """
    is_prime returns True if the given number is a prime number, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        return None
    if n == 1:
        return 2
    
    first = 2
    second = 3
    
    for i in range(3, n+1):
        third = first + second
        first = second
        second = third
        if is_prime(third):
            if i == n:
                return third
        else:
            i -= 1
