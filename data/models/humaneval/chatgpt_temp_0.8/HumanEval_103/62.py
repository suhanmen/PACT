def rounded_avg(n, m):
    if n > m:
        return -1
    
    # calculate the sum of integers from n to m
    total = sum(range(n, m+1))
    
    # calculate the rounded average
    avg = round(total / (m - n + 1))
    
    # convert the average to binary
    binary_avg = bin(avg)
    
    return binary_avg
