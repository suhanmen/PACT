def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2
    else:
        count += 2 * 9 * pow(10, n-2) # Count of numbers that start with 1 or end with 1 but not both
        count += pow(10, n-2) # Count of numbers that start and end with 1
        return count
