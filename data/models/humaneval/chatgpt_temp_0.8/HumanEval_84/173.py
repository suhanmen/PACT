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
    # Convert the integer N to a string and then split it into its digits
    digits = list(str(N))
    # Initialize a variable to hold the sum of the digits
    digit_sum = 0
    # Iterate over the list of digits, converting each to binary and adding the binary value to digit_sum
    for digit in digits:
        binary = bin(int(digit))[2:] # convert the digit to binary and remove the '0b' prefix
        digit_sum += int(binary)
    # Convert the digit_sum to binary and return it as a string
    return bin(digit_sum)[2:]
