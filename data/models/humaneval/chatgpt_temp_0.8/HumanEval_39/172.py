def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        for i in range(2, int(x**(0.5))+1):
            if x % i == 0:
                return False
        return True
    
    def fibonacci(n: int) -> int:
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    
    count = 0
    i = 0
    while count < n:
        i += 1
        if is_prime(fibonacci(i)):
            count += 1
    return fibonacci(i)
