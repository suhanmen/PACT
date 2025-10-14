def solve(N):
    # Convert N to a string to iterate over its digits
    N_str = str(N)
    
    # Initialize the total sum to zero
    total_sum = 0
    
    # Iterate over the digits of N
    for digit in N_str:
        # Convert the digit to an integer and add it to the total sum
        total_sum += int(digit)
    
    # Convert the total sum to a binary string and return it
    return bin(total_sum)[2:]
