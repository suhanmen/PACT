def rounded_avg(n, m):
    if n > m:
        return -1
    
    total = 0
    num_of_integers = m - n + 1
    
    for i in range(n, m+1):
        total += i
    
    average = round(total / num_of_integers)
    binary = bin(average)
    
    return binary
