def prime_fib(n: int):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def fib():
        a, b = 0, 1
        while True:
            yield b
            a, b = b, a + b

    fib_gen = fib()
    count = 0
    while True:
        num = next(fib_gen)
        if is_prime(num):
            count += 1
            if count == n:
                return num
