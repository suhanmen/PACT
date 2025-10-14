def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Count of n-digit numbers that start with 1
    start_count = 9 * 10 ** (n-2) if n > 1 else 1
    
    # Count of n-digit numbers that end with 1
    end_count = 10 ** (n-1)
    
    # Count of n-digit numbers that start and end with 1
    both_count = 1 if n > 1 else 0
    
    return start_count + end_count - both_count
