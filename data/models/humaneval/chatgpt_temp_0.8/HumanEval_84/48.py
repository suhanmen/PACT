def solve(N):
    # Convert N to binary and remove the "0b" prefix
    binary_str = bin(N)[2:]
    
    # Sum the digits in binary
    binary_sum = sum(int(digit) for digit in binary_str)
    
    # Convert the binary sum to a binary string and return it
    return bin(binary_sum)[2:]
