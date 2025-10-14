def rounded_avg(n, m):
    if n > m:
        return -1
    
    average = sum(range(n, m+1)) / (m-n+1)
    rounded_average = round(average)
    binary_average = bin(rounded_average)
    
    return binary_average
