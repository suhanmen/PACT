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
    # Convert the integer to a string to access individual digits
    str_N = str(N)
    
    # Initialize a variable to store the sum of binary digits
    binary_sum = 0
    
    # Iterate over each digit in the string
    for digit in str_N:
        # Convert the digit to binary and count the number of 1's in the binary representation
        binary_sum += bin(int(digit)).count('1')
    
    # Convert the binary sum to a binary string and return it
    return bin(binary_sum)[2:]
