def solve(N):
    binary = bin(N)[2:]  # convert N to binary and remove "0b" prefix
    binary_sum = sum(int(digit) for digit in binary)
    return bin(binary_sum)[2:]  # convert binary sum to string and remove "0b" prefix
