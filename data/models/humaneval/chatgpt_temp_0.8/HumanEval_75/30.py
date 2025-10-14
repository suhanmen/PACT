def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # First, we'll create a list of prime numbers less than 100.
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # Next, we'll check if the given number is the product of 3 prime numbers.
    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
            if count == 3:
                return True
    return False
