def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2
    else:
        count += 2 * 9 * 10**(n-2) # count of n-digit numbers that start with 1 or end with 1
        count += starts_one_ends(n-1) # count of (n-1)-digit numbers that start or end with 1
    return count
