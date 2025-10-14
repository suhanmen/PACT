def solve(N):
    """
    Given a positive integer N, return the total sum of its digits in binary.

    Example:
        For N = 1000, the sum of digits will be 1. The output should be "1".
        For N = 150, the sum of digits will be 6. The output should be "110".
        For N = 147, the sum of digits will be 12. The output should be "1100".

    Variables:
        @N integer
            Constraints: 0 ≤ N ≤ 10000.
    Output:
        A string of binary number.
    """
    # Convert the integer to a binary string and remove the "0b" prefix
    binary_string = bin(N)[2:]
    
    # Calculate the sum of the digits in the binary string
    digit_sum = sum(int(d) for d in binary_string)
    
    # Convert the digit sum to a binary string and return it
    return bin(digit_sum)[2:]
