def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    fibs = [0, 1]
    count = 2
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if is_prime(next_fib):
            if count == n:
                return next_fib
            count += 1
        fibs.append(next_fib)
