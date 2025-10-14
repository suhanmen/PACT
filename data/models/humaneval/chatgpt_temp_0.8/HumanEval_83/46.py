def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2
    elif n > 1:
        count += 9 * (10 ** (n-2)) # counting numbers that start with 1
        count += 9 * (10 ** (n-2)) # counting numbers that end with 1
        count -= 9 # subtracting numbers that start and end with 1
        return count
    else:
        return -1
