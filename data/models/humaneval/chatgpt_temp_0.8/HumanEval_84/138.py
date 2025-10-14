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
    # Convert N to a string
    str_N = str(N)
    
    # Initialize the sum of the digits in binary
    sum_binary = 0
    
    # Loop over each digit in str_N
    for digit in str_N:
        # Convert the digit to an integer and add it to the sum of the digits
        sum_binary += int(digit)
    
    # Convert the sum of the digits to binary and return it as a string
    return bin(sum_binary)[2:]
