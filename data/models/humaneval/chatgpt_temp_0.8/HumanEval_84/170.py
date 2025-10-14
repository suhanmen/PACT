def solve(N):
    binary = bin(N)[2:] # Convert N to binary and remove the '0b' prefix
    sum_of_digits = sum(int(digit) for digit in binary)
    return bin(sum_of_digits)[2:] # Convert the sum of digits to binary and remove the '0b' prefix
