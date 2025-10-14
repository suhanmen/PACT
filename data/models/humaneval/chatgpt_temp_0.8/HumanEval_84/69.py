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
    # Convert the integer to a string, then to a list of digits
    digits = [int(d) for d in str(N)]
    
    # Compute the sum of the digits in binary
    sum_of_digits = sum([int(bin(d)[2:]) for d in digits])
    
    # Convert the sum to a binary string and return it
    return bin(sum_of_digits)[2:]
