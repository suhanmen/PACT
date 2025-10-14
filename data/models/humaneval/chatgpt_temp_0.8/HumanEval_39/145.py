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

    def fibonacci(n):
        if n in [0, 1]:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    count = 0
    num = 2
    while count < n:
        if is_prime(num) and fibonacci(num) == num:
            count += 1
        num += 1
    return num-1
