def solve(N):
    # convert N to binary and remove the "0b" prefix
    binary_str = bin(N)[2:]
    
    # sum up the digits in binary representation of N
    total_sum = sum([int(digit) for digit in binary_str])
    
    # convert the total sum to binary and return it as a string
    return bin(total_sum)[2:]
