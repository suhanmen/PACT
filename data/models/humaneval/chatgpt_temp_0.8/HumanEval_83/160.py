def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    # Count the number of n-digit integers that start with 1
    count += 9**(n-1)
    # Count the number of n-digit integers that end with 1
    count += 9**(n-1)
    # Subtract the overlap (the numbers that both start and end with 1)
    count -= 8**(n-1)
    return count
