def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # First, we need to check if the number a is less than 2 or greater than 100.
    # If it is, we can't use it since we only need numbers less than or equal to 100.
    if a < 2 or a > 100:
        return False
    
    # We will keep count of how many prime factors we have found so far.
    count = 0
    
    # Now, we will check if 2 is a prime factor of a.
    # If it is, we divide it out and increment the count.
    while a % 2 == 0:
        a //= 2
        count += 1
    
    # If we have found 3 prime factors, return True.
    if count == 3:
        return True
    
    # We will do the same for 3 and 5.
    for i in range(3, 6, 2):
        while a % i == 0:
            a //= i
            count += 1
        
        if count == 3:
            return True
    
    # If we reach here, it means we didn't find 3 prime factors.
    return False
