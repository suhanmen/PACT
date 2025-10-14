def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num: int) -> bool:
        """
        is_prime returns True if num is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(num: int) -> int:
        """
        fibonacci returns the num-th number in the Fibonacci sequence.
        """
        if num <= 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibonacci(num-1) + fibonacci(num-2)

    i = 0
    while True:
        i += 1
        num = fibonacci(i)
        if is_prime(num):
            n -= 1
            if n == 0:
                return num
