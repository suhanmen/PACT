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
    def is_prime(num: int):
        """
        Helper function to check if a number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib_seq = [0, 1]  # initialize the Fibonacci sequence
    while len(fib_seq) < n + 1:
        # generate the next Fibonacci number
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)

    for num in fib_seq:
        # check if the number is prime and return it if it is
        if is_prime(num):
            return num
