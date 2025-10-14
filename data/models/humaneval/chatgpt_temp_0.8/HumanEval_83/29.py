def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1  # only 1 number of 1 digit starts or ends with 1
    else:
        count = 9  # there are 9 possible digits (excluding 0) for the first and last position
        for i in range(2, n):
            count *= 10  # for each remaining position, there are 10 possible digits
        return 2 * count  # multiply by 2 to count both cases (start or end with 1)
