def rounded_avg(n, m):
    # Check if n is greater than m
    if n > m:
        return -1
    
    # Compute the sum and count of integers from n through m
    total_sum = sum(range(n, m+1))
    count = m - n + 1
    
    # Compute the average and round to the nearest integer
    avg = round(total_sum / count)
    
    # Convert the rounded average to binary and return as a string
    return bin(avg)
