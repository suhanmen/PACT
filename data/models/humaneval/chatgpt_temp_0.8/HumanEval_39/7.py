def prime_fib(n: int):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    count = 0
    i = 0
    while count < n:
        i += 1
        if is_prime(fibonacci(i)):
            count += 1

    return fibonacci(i)
