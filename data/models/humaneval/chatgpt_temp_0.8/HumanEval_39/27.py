def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num: int):
        """
        Helper function to check if a number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib = [1, 1]
    i = 2
    while i < n:
        fib.append(fib[i-1] + fib[i-2])
        if is_prime(fib[i]):
            i += 1
    return fib[-1]
