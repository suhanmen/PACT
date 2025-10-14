# CANNOT PARSE CODE SNIPPET
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    def fibonacci(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    i = 0
    while True:
        fib = fibonacci(i)
        if is_prime(fib):
            n -= 1
            if n == 0:
                return fib
        i += 1
