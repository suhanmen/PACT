def solve(N):
    # convert the integer to binary string and remove the '0b' prefix
    binary_str = bin(N)[2:]
    
    # sum the digits in the binary string
    binary_sum = sum(int(digit) for digit in binary_str)
    
    # convert the binary sum to binary string and return it
    return bin(binary_sum)[2:]
