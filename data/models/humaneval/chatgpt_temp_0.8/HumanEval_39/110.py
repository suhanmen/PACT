# CANNOT PARSE CODE SNIPPET
def is_prime(num: int) -> bool:
    """
    is_prime returns True if num is prime, else False.
    """
    if num < 2:  # numbers less than 2 are not prime
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    if n == 1:
        return 2
    if n == 2:
        return 3
    
    # initializing first two Fibonacci numbers
    f1, f2 = 2, 3
    count = 3  # count is 3 because first two numbers are already checked
    
    while count <= n:
        # generating next Fibonacci number
        f3 = f1 + f2
        # checking if the Fibonacci number is prime
        if is_prime(f3):
            # incrementing the counter
            count += 1
            # updating the values of f1 and f2
            f1, f2 = f2, f3
        else:
            # updating the values of f1 and f2
            f1, f2 = f2, f3
    
    return f3
