def solve(N):
    # Convert N to a string and then to binary string
    binary = bin(N)[2:]
    # Initialize sum of digits to 0
    digit_sum = 0
    # Loop over each character in the binary string and add the integer value to digit_sum
    for digit in binary:
        digit_sum += int(digit)
    # Convert digit_sum to binary and return as a string
    return bin(digit_sum)[2:]
