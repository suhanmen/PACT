def prime_fib(n: int):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib = [1, 1]
    while True:
        next_fib = fib[-1] + fib[-2]
        if is_prime(next_fib):
            n -= 1
            if n == 0:
                return next_fib
        fib.append(next_fib)
