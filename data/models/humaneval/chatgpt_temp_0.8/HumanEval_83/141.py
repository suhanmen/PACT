def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2 # 1 and 0 are both valid one-digit numbers that start or end with 1.
    else:
        count = 10**(n-1) # all n-digit numbers with 1 as the first digit
        count += 10**(n-2) * 9 # add all n-digit numbers with 1 as the last digit
        return count
