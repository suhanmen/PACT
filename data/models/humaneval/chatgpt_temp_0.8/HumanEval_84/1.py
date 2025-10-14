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
    # Convert N to binary string and remove the "0b" prefix
    binary_str = bin(N)[2:]
    
    # Initialize sum to 0
    total_sum = 0
    
    # Loop through each digit in the binary string
    for digit in binary_str:
        # Convert digit to integer and add to the total sum
        total_sum += int(digit)
    
    # Convert total sum to binary string and return
    return bin(total_sum)[2:]
