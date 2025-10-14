def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i*i <= num:
            if num % i == 0 or num % (i+2) == 0:
                return False
            i += 6
        return True

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    i = 0
    while True:
        num = fibonacci(i)
        if is_prime(num):
            n -= 1
            if n == 0:
                return num
        i += 1
