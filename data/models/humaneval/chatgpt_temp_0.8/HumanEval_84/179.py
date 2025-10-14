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
    # convert N to binary string, then iterate through each character and sum the ones
    binary_str = bin(N)[2:] # remove the '0b' prefix from binary string
    ones_sum = sum(int(x) for x in binary_str)
    
    # convert ones_sum to binary string and return
    return bin(ones_sum)[2:]
