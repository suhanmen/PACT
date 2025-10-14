def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2 # 1 and 10
    else:
        count = 9 # for numbers that start with 1
        for i in range(n-2):
            count *= 10
        count += 9 # for numbers that end with 1
        return count
