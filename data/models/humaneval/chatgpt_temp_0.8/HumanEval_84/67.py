def solve(N):
    # convert N to binary and remove the '0b' prefix
    binary_str = bin(N)[2:]
    # initialize the sum of digits to 0
    digit_sum = 0
    # iterate through each digit in binary_str
    for digit in binary_str:
        # add the integer value of the digit to digit_sum
        digit_sum += int(digit)
    # convert digit_sum to binary and return as a string
    return bin(digit_sum)[2:]
