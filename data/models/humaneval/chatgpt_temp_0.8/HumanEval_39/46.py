def prime_fib(n: int):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b, count = 2, 3, 2
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1
    return b
