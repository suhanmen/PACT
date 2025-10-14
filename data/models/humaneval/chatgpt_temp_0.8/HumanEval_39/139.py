def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    if n == 1:
        return 2
    elif n == 2:
        return 3
    
    a, b = 2, 3
    prime_fib_count = 2
    
    while prime_fib_count < n:
        a, b = b, a + b
        if is_prime(b):
            prime_fib_count += 1
    
    return b
