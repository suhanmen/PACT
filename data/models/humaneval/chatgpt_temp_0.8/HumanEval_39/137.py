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
        """
        Helper function to check if a number is prime.
        """
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    # Initialize the Fibonacci sequence with the first two numbers
    fib_seq = [1, 1]

    # Keep generating new Fibonacci numbers until we find one that is prime
    while True:
        # Generate the next Fibonacci number
        next_fib = fib_seq[-1] + fib_seq[-2]

        # Check if the new Fibonacci number is prime
        if is_prime(next_fib):
            # If it is, add it to the sequence and break out of the loop
            fib_seq.append(next_fib)
            break

        # If it's not, add it to the sequence and continue generating the next number
        fib_seq.append(next_fib)

    # Return the nth prime Fibonacci number
    return fib_seq[n-1]
