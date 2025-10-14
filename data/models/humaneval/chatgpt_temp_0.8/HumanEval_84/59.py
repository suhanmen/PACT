def solve(N):
    # Convert N to a string and then to binary string
    binary_str = bin(N)[2:]
    
    # Sum the digits in the binary string
    sum_of_digits = sum(int(digit) for digit in binary_str)
    
    # Convert the sum to binary string and return
    return bin(sum_of_digits)[2:]
