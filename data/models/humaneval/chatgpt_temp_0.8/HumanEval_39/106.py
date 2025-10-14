def prime_fib(n: int):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def fibonacci(num):
        if num <= 1:
            return num
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

    i = 1
    count = 0
    while count < n:
        i += 1
        fib = fibonacci(i)
        if is_prime(fib):
            count += 1
    return fib
