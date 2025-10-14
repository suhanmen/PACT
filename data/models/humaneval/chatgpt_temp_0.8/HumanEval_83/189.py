def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2 # 1 and 11
    else:
        count += 9 * (10 ** (n - 2)) * 2 # count of numbers starting with 1 and ending with any digit other than 1
        count += 10 ** (n - 1) # count of numbers ending with 1
    return count
