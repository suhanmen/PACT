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
    # Convert N to a string and iterate over its digits
    digits_sum = 0
    for digit in str(N):
        digits_sum += int(digit)
        
    # Convert the sum of digits to binary
    binary_sum = bin(digits_sum)[2:]
    
    return binary_sum
