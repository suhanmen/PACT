def is_prime(n):
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """Function to check if the given number is the multiplication of 3 prime numbers"""
    if a < 2:
        return False
    primes = [i for i in range(2, 100) if is_prime(i)] # generate list of primes less than 100
    count = 0
    for p in primes:
        if a % p == 0: # check if prime number divides the given number
            count += 1
    return count == 3 # return True if exactly 3 prime numbers divide the given number
