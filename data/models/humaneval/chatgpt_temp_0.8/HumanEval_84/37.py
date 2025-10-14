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
    # Convert N to a string so we can iterate through its digits
    N_str = str(N)
    
    # Initialize a sum variable to keep track of the sum of digits
    digit_sum = 0
    
    # Iterate through each digit in N
    for digit in N_str:
        # Convert the digit to an integer and add it to the sum
        digit_sum += int(digit)
    
    # Convert the sum of digits to binary and return it as a string
    return bin(digit_sum)[2:]
