def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib_nums = [0, 1]
    i = 2
    while i <= n:
        next_num = fib_nums[-1] + fib_nums[-2]
        if is_prime(next_num):
            i += 1
            if i == n:
                return next_num
        fib_nums.append(next_num)
