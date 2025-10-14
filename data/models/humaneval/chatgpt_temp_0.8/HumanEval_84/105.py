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
    # Convert N to binary and remove the "0b" prefix
    binary_str = bin(N)[2:]
    
    # Sum the digits of the binary string
    binary_sum = sum(int(digit) for digit in binary_str)
    
    # Convert the binary sum to a binary string and return it
    return bin(binary_sum)[2:]
