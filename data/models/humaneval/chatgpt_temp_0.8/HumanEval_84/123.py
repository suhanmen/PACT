def solve(N):
    # Convert the integer to binary string
    binary_str = bin(N)[2:]
    
    # Calculate the sum of digits in the binary string
    sum_of_digits = sum(int(digit) for digit in binary_str)
    
    # Convert the sum to binary string and return
    return bin(sum_of_digits)[2:]
