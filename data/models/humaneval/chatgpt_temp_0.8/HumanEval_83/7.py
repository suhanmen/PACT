def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    count = 9  # There are nine choices for the first digit (1-9)
    for i in range(1, n):
        count += 9 * 10**(i-1)  # There are nine choices for each subsequent digit
    return count
