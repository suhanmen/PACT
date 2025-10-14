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
    
    fib_list = [0, 1]
    count = 2
    while True:
        next_fib = fib_list[count-1] + fib_list[count-2]
        if is_prime(next_fib):
            if n == 1:
                return next_fib
            n -= 1
        count += 1
