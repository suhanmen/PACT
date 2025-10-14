def solve(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.

    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".

    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """

    binary_sum = 0

    # Convert N to a string and loop through each character
    for digit in str(N):
        # Convert the digit back to an integer and add it to the binary sum
        binary_sum += int(digit)

    # Convert the binary sum to a string in binary format and return it
    return bin(binary_sum)[2:]
