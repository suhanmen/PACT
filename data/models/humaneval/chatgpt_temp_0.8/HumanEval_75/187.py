def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Initializing the prime numbers list
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # Initializing the counter
    counter = 0
    
    # Checking if the given number is divisible by any 3 prime numbers
    for i in primes:
        if a % i == 0:
            counter += 1
            if counter == 3:
                return True
    return False
