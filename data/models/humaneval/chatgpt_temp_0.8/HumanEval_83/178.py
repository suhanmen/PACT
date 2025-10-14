def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # count the number of numbers that start with 1
        count += 9 * 10**(n-2)
        # count the number of numbers that end with 1
        count += 9 * 10**(n-2)
        # count the number of numbers that start and end with 1
        count += 10**(n-2)
        return count
