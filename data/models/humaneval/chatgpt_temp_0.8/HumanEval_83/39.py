def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n < 1:
        return count
    elif n == 1:
        return 1
    else:
        count += 9  # Count of numbers starting with 1
        count += 9  # Count of numbers ending with 1
        count -= 1  # Count of number 11 which is counted twice
        count += starts_one_ends(n-1) * 8  # Count of numbers with 1 at second position
        return count
