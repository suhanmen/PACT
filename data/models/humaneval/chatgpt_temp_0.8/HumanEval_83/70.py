def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        # If n is 1, there is only one n-digit number, i.e., 1.
        count = 1
    else:
        # If n > 1, count the number of n-digit numbers that start or end with 1.
        count = 9*(10**(n-2)) + 2*(9**(n-1))
    return count
