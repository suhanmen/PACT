def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(10**(n-1), 10**n):
        num_str = str(i)
        if num_str.startswith('1') or num_str.endswith('1'):
            count += 1
    return count
