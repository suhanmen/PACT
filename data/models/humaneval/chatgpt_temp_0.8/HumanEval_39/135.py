def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(num: int) -> int:
        if num == 1:
            return 2
        elif num == 2:
            return 3
        else:
            fib1 = 2
            fib2 = 3
            for i in range(3, num + 1):
                fib3 = fib1 + fib2
                fib1 = fib2
                fib2 = fib3
            return fib2

    count = 1
    i = 1
    while count <= n:
        num = fibonacci(i)
        if is_prime(num):
            if count == n:
                return num
            count += 1
        i += 1
