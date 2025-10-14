def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2 # 1 and 10
    else:
        count += 9 * (10**(n-2)) # count of n-digit numbers that start with 1
        count += 9 * (10**(n-2)) # count of n-digit numbers that end with 1
        count -= 9 # count of n-digit numbers that start and end with 1 (counted twice)
        return count
