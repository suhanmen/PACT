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
    str_N = str(N)
    
    # Initialize the sum of digits to zero
    sum_of_digits = 0
    
    # Iterate through each digit of N and add it to the sum of digits
    for digit in str_N:
        sum_of_digits += int(digit)
    
    # Convert the sum of digits to a binary string
    binary_sum = bin(sum_of_digits)[2:]
    
    # Return the binary string
    return binary_sum
