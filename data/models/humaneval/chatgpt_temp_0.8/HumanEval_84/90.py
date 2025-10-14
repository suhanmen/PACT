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
    # Convert N to a string so we can iterate over the digits
    s = str(N)
    # Initialize a variable to hold the sum of the digits
    digit_sum = 0
    # Loop over the digits and add them to digit_sum
    for c in s:
        digit_sum += int(c)
    # Convert digit_sum to a binary string and return it
    return bin(digit_sum)[2:]
