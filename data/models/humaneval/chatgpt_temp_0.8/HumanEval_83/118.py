def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 1  # Special case for n = 1
    else:
        count += 9  # Count 1 to 9 as starting digit
        count += 9 * (10**(n-2))  # Count all other n-1 digit numbers that start with 1
        count += 9 * (10**(n-2))  # Count all other n-1 digit numbers that end with 1
    return count
