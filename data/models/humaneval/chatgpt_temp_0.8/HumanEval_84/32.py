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
    # Convert the integer to a string and then iterate over each character
    digit_sum = 0
    for digit in str(N):
        # Convert each digit to binary and count the number of "1"s
        binary_digit = bin(int(digit))[2:]  # [2:] is to remove the "0b" prefix
        digit_sum += binary_digit.count("1")
    
    # Convert the sum to binary and return the result as a string
    return bin(digit_sum)[2:]  # [2:] is to remove the "0b" prefix
