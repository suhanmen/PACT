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
    # Convert number to binary string
    binary_string = bin(N)[2:]
    
    # Initialize sum variable
    digit_sum = 0

    # Iterate through binary string and add each digit to sum
    for digit in binary_string:
        digit_sum += int(digit)
    
    # Convert digit sum to binary string and return
    return bin(digit_sum)[2:]
