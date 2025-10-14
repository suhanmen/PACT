def solve(N):
    # Convert N to binary string and remove the "0b" prefix
    binary_string = bin(N)[2:]
    
    # Calculate the sum of digits in binary string
    binary_sum = sum(int(digit) for digit in binary_string)
    
    # Convert the binary sum to binary string and return it
    return "{0:b}".format(binary_sum)
