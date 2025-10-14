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
    # Convert the integer to a string so we can loop through its digits
    digits = str(N)
    
    # Initialize a variable to hold the sum of the digits
    digit_sum = 0
    
    # Loop through each digit in the string, convert to binary and add to digit_sum
    for digit in digits:
        digit_sum += int(bin(int(digit))[2:])
    
    # Convert digit_sum to a binary string and return it
    return bin(digit_sum)[2:]
