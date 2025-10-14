def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if a is less than 2, return False if so
    if a < 2:
        return False
    
    # Initialize a list to store prime numbers
    primes = []
    
    # Loop through numbers from 2 to 100 (inclusive)
    for i in range(2, 101):
        # Check if i is prime
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    
    # Check if a is the product of 3 prime numbers
    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
        if count == 3:
            return True
    
    return False
