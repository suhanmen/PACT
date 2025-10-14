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
    # Convert N to a string to be able to iterate through its digits
    N_str = str(N)
    
    # Initialize the sum of digits to 0
    digit_sum = 0
    
    # Iterate through each digit in N_str
    for digit in N_str:
        # Convert the digit to binary and count the number of "1"s in the binary representation
        # Add that count to the digit_sum
        digit_sum += bin(int(digit)).count("1")
    
    # Convert the digit_sum to a binary string and return it
    return bin(digit_sum)[2:]
