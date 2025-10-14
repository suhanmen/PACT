def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function to check if a number is the multiplication of 3 prime numbers"""
    primes = []
    for i in range(2, 100):
        if is_prime(i):
            primes.append(i)
    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
    if count == 3:
        return True
    else:
        return False
