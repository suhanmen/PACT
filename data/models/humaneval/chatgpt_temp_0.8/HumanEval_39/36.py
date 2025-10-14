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
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    if n <= 0:
        return None
    elif n == 1:
        return 2
    else:
        first_num = 2
        second_num = 3
        count = 2
        while True:
            third_num = first_num + second_num
            if is_prime(third_num):
                count += 1
                if count == n:
                    return third_num
            first_num = second_num
            second_num = third_num
