def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2
    else:
        count += 9 * (10 ** (n-2)) * 2  # count of numbers that start with 1 and end with a digit between 0 and 9 (excluding 1)
        count += starts_one_ends(n-1)  # count of numbers that start with 1 and end with 1
    return count
