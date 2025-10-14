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
    # Convert N to a string to easily access each digit
    N_str = str(N)
    
    # Initialize a variable to keep track of the sum of digits
    digit_sum = 0
    
    # Loop through each digit in N_str 
    for digit in N_str:
        # Convert the digit to an integer and add it to digit_sum
        digit_sum += int(digit)
    
    # Convert digit_sum to binary using the format method
    binary_sum = "{0:b}".format(digit_sum)
    
    # Return the binary_sum
    return binary_sum
