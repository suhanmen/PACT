def solve(N):
    # Convert N to binary string and remove "0b" prefix
    binary_str = bin(N)[2:]
    
    # Convert each character in binary string to integer and sum them
    digit_sum = sum(int(digit) for digit in binary_str)
    
    # Convert digit sum to binary string and return
    return bin(digit_sum)[2:]
