def rounded_avg(n, m):
    if n > m:
        return -1
    
    avg = round((n + m) / 2) # compute the average and round to nearest integer
    binary_avg = bin(avg) # convert to binary
    
    return binary_avg
