def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100.
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # check if number is less than 2 or greater than 100
    if a < 2 or a > 100:
        return False
    
    # count the number of prime factors
    count = 0
    for i in range(2, a+1):
        while a % i == 0:
            count += 1
            a //= i
        if count > 3: # if we have more than 3 prime factors, return False
            return False
        if a == 1: # if we have found 3 prime factors, return True
            return count == 3
    return False # if we haven't found 3 prime factors by the end, return False
