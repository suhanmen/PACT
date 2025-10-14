def is_multiply_prime(a):
    """
    Returns True if the given number is the multiplication of 3 prime numbers and False otherwise.
    """
    # Create a list of prime numbers less than or equal to 100
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # Check if the given number is the multiplication of 3 prime numbers
    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
        if count == 3:
            return True
    return False
