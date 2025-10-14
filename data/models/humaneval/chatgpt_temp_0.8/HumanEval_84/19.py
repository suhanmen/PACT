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
    
    # convert the number to a string and then to a list of its digits
    digits = list(str(N))
    
    # convert each digit to its binary representation and sum them up
    total = sum([int(bin(int(d))[2:]) for d in digits])
    
    # convert the total to a binary string and return it
    return bin(total)[2:]
