def solve(N):
    binary = bin(N)[2:] # convert N to binary and remove prefix "0b"
    binary_sum = sum(int(digit) for digit in binary)
    return bin(binary_sum)[2:] # convert binary_sum to binary and remove prefix "0b"
