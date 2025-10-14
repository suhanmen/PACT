# CANNOT PARSE CODE SNIPPET
def prime_fib(n: int) -> int:
    def is_prime(x: int) -> bool:
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    def fib(n: int) -> int:
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)
    
    count = 0
    i = 0
    while count < n:
        i += 1
        x = fib(i)
        if is_prime(x):
            count += 1
    return x
