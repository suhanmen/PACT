def rounded_avg(n, m):
    if n > m:
        return -1
  
    # Calculate the sum of integers from n through m
    total = sum(range(n, m+1))
  
    # Calculate the average
    avg = total / (m - n + 1)
  
    # Round to the nearest integer and convert to binary
    result = round(avg)
    result = bin(result)
  
    return result
