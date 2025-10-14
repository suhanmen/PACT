import math

def rounded_avg(n, m):
    # Check if n is greater than m
    if n > m:
        return -1
    
    # Compute the sum of integers from n through m
    sum = 0
    for i in range(n, m+1):
        sum += i
    
    # Compute the rounded average
    avg = round(sum / (m-n+1))
    
    # Convert the rounded average to binary
    binary_avg = bin(avg)
    
    return binary_avg
