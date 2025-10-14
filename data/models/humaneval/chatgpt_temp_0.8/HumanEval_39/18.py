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
    
    f1, f2 = 1, 1
    count = 2  # start from 2 because we already know the first two are prime
    while count < n:
        f3 = f1 + f2
        if is_prime(f3):
            count += 1
        f1, f2 = f2, f3
    
    return f3 if is_prime(f3) else prime_fib(n+1)
