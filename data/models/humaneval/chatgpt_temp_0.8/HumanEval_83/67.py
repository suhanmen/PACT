def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0

    # Count the number of n-digit integer that start with 1
    count += 9 * (10 ** (n-2)) if n > 1 else 1

    # Count the number of n-digit integer that end with 1
    count += 10 ** (n-1) - (10 ** (n-2))

    # Count the number of n-digit integer that start and end with 1
    count -= 10 ** (n-2)

    return count
