def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    
    count = 0
    # Count numbers that start with 1
    count += 9 * 10 ** (n - 2)  # First digit can be anything but 0 or 1, remaining digits can be anything
    # Count numbers that end with 1
    count += 10 ** (n - 1)  # Last digit must be 1, remaining digits can be anything
    
    # If n > 2, count numbers that start and end with 1
    if n > 2:
        count -= 9  # Subtract cases where all digits are 1
    
    return count
