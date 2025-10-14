def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    
    if n == 1:
        return 2
    
    count += 9 * (10 ** (n-2)) # count of first digit being 1
    count += 9 * (10 ** (n-2)) # count of last digit being 1
    count -= 8 # count of numbers with first and last digit being 1
    
    return count
