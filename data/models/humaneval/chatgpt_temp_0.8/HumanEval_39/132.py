def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    a, b = 1, 1
    count = 0
    while True:
        if is_prime(a) and count == n - 1:
            return a
        elif is_prime(a):
            count += 1
        a, b = b, a + b
