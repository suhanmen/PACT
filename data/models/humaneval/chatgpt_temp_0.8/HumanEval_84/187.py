def solve(N):
    binary = bin(N)[2:] # convert N to binary string (without leading '0b')
    total = sum(int(digit) for digit in binary) # sum the digits in binary
    return bin(total)[2:] # convert the total to binary string (without leading '0b') and return it as output
