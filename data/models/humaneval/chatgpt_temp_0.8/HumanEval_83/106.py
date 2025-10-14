def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2  # 1 and 10 are the only 1-digit numbers that start or end with 1
    else:
        count += 9 * 2  # 1-9 numbers can start or end with 1
        for i in range(2, n):
            count += 9 * 10 ** (i - 2) * 2  # middle digits can be any of 0-9
        count += 10  # last digit can be any of 0-9
    return count
