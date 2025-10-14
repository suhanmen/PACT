# CANNOT PARSE CODE SNIPPET
def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num):
        """
        Returns True if the number is prime, False otherwise.
        """
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def fibonacci(num):
        """
        Returns the num-th number in the Fibonacci sequence.
        """
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)
        
    i = 2
    while True:
        fib = fibonacci(i)
        if is_prime(fib):
            if n == 1:
                return fib
            n -= 1
        i += 1
