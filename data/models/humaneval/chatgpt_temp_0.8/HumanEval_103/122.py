def rounded_avg(n, m):
    if n > m:
        return -1
    avg = sum(range(n, m + 1)) / (m - n + 1)
    rounded_avg = round(avg)
    binary_avg = bin(rounded_avg)
    return binary_avg
