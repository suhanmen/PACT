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
            if n == 1:
                return next_fib
            else:
                n -= 1
        fib.append(next_fib)
