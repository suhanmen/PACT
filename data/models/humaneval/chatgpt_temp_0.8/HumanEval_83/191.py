def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2 # There are two 1-digit numbers that start or end with 1: 1 and 10.
    else:
        count += 9 ** (n-1) # The first digit can be any digit except 0 or 1.
        count += 9 ** (n-2) * 2 # The last digit can be either 0 or 1, so there are 2 choices.
    return count
