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
    # Convert integer N to a string to be able to iterate over its digits
    digits = str(N)
    # Initialize binary_sum variable to store the sum of digits in binary
    binary_sum = 0
    # Iterate over each digit in the string, add it to the binary_sum variable in binary form
    for digit in digits:
        binary_sum += int(bin(int(digit))[2:])
    # Convert the final binary_sum variable to a binary string and return it
    return bin(binary_sum)[2:]
