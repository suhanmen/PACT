def prime_fib(n: int):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    count = 0
    i = 2
    while True:
        if is_prime(fibonacci(i)):
            count += 1
            if count == n:
                return fibonacci(i)
        i += 1
