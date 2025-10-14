def solve(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.

    Example
    -------
    For N = 1000, the sum of digits will be 1 the output should be "1".
    For N = 150, the sum of digits will be 6 the output should be "110".
    For N = 147, the sum of digits will be 12 the output should be "1100".

    Parameters
    ----------
    N : int
        Constraints: 0 ≤ N ≤ 10000.

    Returns
    -------
    str
        A string of binary number
    """
    # Calculate the sum of digits of N
    sum_digits = sum(int(digit) for digit in str(N))

    # Convert sum of digits to binary and return as string
    return bin(sum_digits)[2:]
