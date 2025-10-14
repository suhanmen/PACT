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
    # Convert integer to string to iterate through its digits
    str_N = str(N)
    
    # Initialize binary sum to 0
    bin_sum = 0
    
    # Iterate through each digit and add it to the binary sum
    for digit in str_N:
        bin_sum += int(digit)
    
    # Convert binary sum to binary string and return
    return bin(bin_sum)[2:]
