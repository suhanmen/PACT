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
    
    # Convert N to a string and split it into individual digits
    digits = list(str(N))
    
    # Convert each digit to binary and sum them up
    binary_sum = 0
    for digit in digits:
        binary_sum += bin(int(digit))[2:]
    
    # Convert the sum to binary and return it
    return bin(binary_sum)[2:]
