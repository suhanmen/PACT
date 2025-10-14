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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # initialize the first two numbers of the Fibonacci sequence
        fib1, fib2 = 1, 1
        count = 2
        while count < n:
            # calculate the next Fibonacci number
            fib3 = fib1 + fib2
            # check if it's prime
            is_prime = True
            for i in range(2, int(fib3 ** 0.5) + 1):
                if fib3 % i == 0:
                    is_prime = False
                    break
            # if it's prime, increment the count
            if is_prime:
                count += 1
            # update the Fibonacci numbers for the next iteration
            fib1, fib2 = fib2, fib3
        return fib3
