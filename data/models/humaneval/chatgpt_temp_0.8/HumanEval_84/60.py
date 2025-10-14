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
    # Convert the integer to a string and then convert each digit to binary
    binary_digits = [bin(int(d))[2:] for d in str(N)]
    
    # Sum the binary digits and convert the sum to binary
    binary_sum = bin(sum([int(d, 2) for d in binary_digits]))[2:]
    
    # Return the binary sum as a string
    return binary_sum
