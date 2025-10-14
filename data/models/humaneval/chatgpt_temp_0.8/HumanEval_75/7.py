def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if a is less than or equal to 1
    if a <= 1:
        return False
    
    # Create a list of prime numbers less than or equal to 100
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # Check if a is divisible by 3 prime numbers
    num_primes = 0
    for prime in primes:
        if a % prime == 0:
            num_primes += 1
            if num_primes == 3:
                return True
    return False
