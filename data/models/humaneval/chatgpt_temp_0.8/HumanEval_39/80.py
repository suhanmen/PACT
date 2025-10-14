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
        Helper function that checks whether a number is prime or not.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    def fibonacci(num):
        """
        Helper function that generates the num-th Fibonacci number.
        """
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibonacci(num-1) + fibonacci(num-2)
        
    i = 0
    count = 0
    while count < n:
        i += 1
        fib_num = fibonacci(i)
        if is_prime(fib_num):
            count += 1
    return fib_num
