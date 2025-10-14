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
    # Convert the integer to a string and iterate over its digits
    binary_sum = 0
    for digit in str(N):
        # Convert each digit to binary, sum the binary digits, and add to total sum
        binary_sum += sum(int(b) for b in bin(int(digit))[2:])
    # Convert the total sum to binary and return as a string
    return bin(binary_sum)[2:]
