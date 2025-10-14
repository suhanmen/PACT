def is_prime(n):
    """Helper function to determine if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Function to return an array of the first n prime numbers less than n"""
    primes = []
    num = 2
    while len(primes) < n and num < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
