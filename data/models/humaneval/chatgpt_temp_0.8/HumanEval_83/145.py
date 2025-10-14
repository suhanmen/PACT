def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:  # If n is 1, there are only 9 numbers that start or end with 1.
        count = 9
    else:  # If n is greater than 1, use math to calculate the number of valid n-digit numbers.
        count = 18 * (10 ** (n - 2))
    return count
