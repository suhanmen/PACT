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
    # Convert integer N to string and get its length
    num_digits = len(str(N))
    
    # Initialize a sum variable
    digit_sum = 0
    
    # Loop through each digit in the number
    for i in range(num_digits):
        # Get the i-th digit from the right
        digit = (N // 10**i) % 10
        
        # Add the digit to the sum
        digit_sum += digit
    
    # Convert the sum to binary and return as a string
    return bin(digit_sum)[2:]
