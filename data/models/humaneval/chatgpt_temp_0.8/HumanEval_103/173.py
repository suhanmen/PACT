def rounded_avg(n, m):
    if n > m:
        return -1
    
    total = sum(range(n, m+1))
    average = round(total / (m-n+1))
    
    return bin(average)
