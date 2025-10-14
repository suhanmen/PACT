def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:  # special case for 1-digit numbers
        return 2
    else:
        count += 9 * 2  # count of n-digit numbers that start or end with 1
        for i in range(n-2):
            count += 9 * (10 ** i) * 2  # count of (n-i-2)-digit numbers that start or end with 1
        return count
