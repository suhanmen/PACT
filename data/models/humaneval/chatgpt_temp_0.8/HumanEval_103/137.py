def rounded_avg(n, m):
    if n > m:
        return -1
    
    # calculate sum of integers from n through m
    total = sum(range(n, m+1))
    
    # calculate average and round to nearest integer
    average = round(total / (m - n + 1))
    
    # convert average to binary and return result
    return bin(average)
