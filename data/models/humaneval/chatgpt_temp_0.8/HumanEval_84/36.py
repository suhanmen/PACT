def solve(N):
    # Convert N to binary and remove the prefix '0b'
    binary_n = bin(N)[2:]
    
    # Calculate the sum of the digits in binary_n
    binary_sum = sum(int(digit) for digit in binary_n)
    
    # Convert binary_sum to binary and return the result
    return bin(binary_sum)[2:]
