def solve(N):
    # Convert the integer to binary string
    binary_str = bin(N)[2:]
    
    # Calculate the sum of digits in binary
    sum_binary_digits = sum(int(digit) for digit in binary_str)
    
    # Convert the sum to binary string format
    binary_sum = bin(sum_binary_digits)[2:]
    
    return binary_sum
