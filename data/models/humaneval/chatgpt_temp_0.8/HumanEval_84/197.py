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
    # Convert the integer to a string so we can iterate over its digits
    str_num = str(N)
    
    # Initialize the sum of digits to 0
    digit_sum = 0
    
    # Iterate over each digit in the string
    for digit in str_num:
        # Add the integer value of the digit to the digit sum
        digit_sum += int(digit)
    
    # Convert the digit sum to binary and return it as a string
    return bin(digit_sum)[2:]
