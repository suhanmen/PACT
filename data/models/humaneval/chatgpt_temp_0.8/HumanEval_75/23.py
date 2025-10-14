def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    prime_factors = []
    
    # Find prime factors of the number
    for prime in primes:
        while a % prime == 0:
            prime_factors.append(prime)
            a //= prime
    
    # Check if there are exactly 3 prime factors
    return len(prime_factors) == 3
