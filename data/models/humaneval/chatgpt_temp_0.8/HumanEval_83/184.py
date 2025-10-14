def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    # Count of n-digit numbers starting with 1
    count_start = 9 * pow(10, n - 2) if n > 1 else 1
    # Count of n-digit numbers ending with 1
    count_end = 9 * pow(10, n - 2) if n > 1 else 1
    
    count = count_start + count_end
    
    return count
