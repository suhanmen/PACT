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
    # Convert the integer to binary and remove the '0b' prefix
    binary_n = bin(N)[2:]

    # Calculate the sum of digits in binary
    sum_of_digits = sum(int(digit) for digit in binary_n)

    # Convert the sum of digits to binary and return as a string
    return bin(sum_of_digits)[2:]
