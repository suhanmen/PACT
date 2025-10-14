def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round((n+m)/2)
    binary_avg = bin(avg)
    return binary_avg
