def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
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
    # Convert N to a string and iterate over each character
    binary_sum = 0
    for digit in str(N):
        # Convert the digit to binary and add it to the binary sum
        binary_sum += bin(int(digit))[2:]

    # Convert the binary sum back to a string and return it
    return str(binary_sum)
