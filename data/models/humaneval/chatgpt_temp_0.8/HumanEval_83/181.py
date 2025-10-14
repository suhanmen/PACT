def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1     # Only one digit numbers that start or end with 1

    count = 9     # Numbers that start with 1 (excluding 1 itself)
    for i in range(2, n+1):
        count += 9 * (10**(i-2))    # Numbers that end with 1
        count += 9 * (10**(i-2))    # Numbers that start with 1 and end with 1

    return count
