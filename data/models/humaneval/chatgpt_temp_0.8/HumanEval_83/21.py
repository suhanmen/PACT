def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1: # special case for one-digit numbers
        return 2
    else:
        count += 9 * (10 ** (n-2)) # counts numbers that start with 1
        count += 9 * (10 ** (n-2)) # counts numbers that end with 1
        count -= 9 # subtracts the overlap (i.e. numbers that start AND end with 1)
        return count
