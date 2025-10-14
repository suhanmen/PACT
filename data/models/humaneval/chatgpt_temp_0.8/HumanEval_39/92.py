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

    if n < 1:
        return None

    fib_0 = 0
    fib_1 = 1
    count = 0

    while True:
        if is_prime(fib_0):
            count += 1
            if count == n:
                return fib_0

        fib_0, fib_1 = fib_1, fib_0 + fib_1
