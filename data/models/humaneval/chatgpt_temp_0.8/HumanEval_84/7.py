def solve(N):
    # Convert N to a string and then to binary
    binary_str = bin(N)[2:]
    
    # Calculate the sum of the digits in binary
    binary_sum = sum(int(x) for x in binary_str)
    
    # Convert the binary sum to a binary string and return it
    return bin(binary_sum)[2:]
