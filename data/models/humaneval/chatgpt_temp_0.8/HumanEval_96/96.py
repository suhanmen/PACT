def is_prime_number(n):
    """Helper function to check if the given number is prime or not"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Function to return an array of the first n prime numbers less than n"""
    primes = []
    for i in range(2, n):
        if is_prime_number(i):
            primes.append(i)
            if len(primes) == n:
                break
    return primes
