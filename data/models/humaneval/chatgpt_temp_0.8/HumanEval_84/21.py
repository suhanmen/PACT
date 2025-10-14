def solve(N):
    # Convert N to binary and remove the "0b" prefix
    binary = bin(N)[2:]
    
    # Initialize sum to 0
    total = 0
    
    # Loop through each digit in binary and add it to the sum
    for digit in binary:
        total += int(digit)
    
    # Convert the sum to a binary string and return it
    return bin(total)[2:]
