def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    
    # Case when n is 1
    if n == 1:
        return 2
    
    # Count the number of integers that start or end with 1 for all other values of n
    count += 9 * (10 ** (n-2)) * 2   # Count of integers that start with 1 and end with a digit other than 1
    count += 10 ** (n-2)            # Count of integers that start with 1 and end with 1
    count += 10 ** (n-2)            # Count of integers that end with 1 and start with a digit other than 1
    
    return count
