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
    
    # initialize the first two Fibonacci numbers
    fib_numbers = [0, 1]
    
    # compute the next Fibonacci numbers until we get n prime ones
    prime_fib_numbers = []
    while len(prime_fib_numbers) < n:
        # compute the next Fibonacci number
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        # if the next Fibonacci number is prime, add it to the list of prime Fibonacci numbers
        if is_prime(next_fib):
            prime_fib_numbers.append(next_fib)
        # add the next Fibonacci number to the list of Fibonacci numbers
        fib_numbers.append(next_fib)
    
    return prime_fib_numbers[-1]
