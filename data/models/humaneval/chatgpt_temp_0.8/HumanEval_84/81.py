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
    # Convert N to a list of integers representing each digit
    digits = [int(d) for d in str(N)]
    
    # Calculate the sum of the digits in binary
    total = sum(digits)
    binary_total = bin(total)[2:]  # Convert to binary and remove the '0b' prefix
    
    return binary_total
