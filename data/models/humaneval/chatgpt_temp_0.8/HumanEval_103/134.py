def rounded_avg(n, m):
    if n > m:
        return -1
    avg = (n + m) / 2
    rounded = round(avg)
    return bin(rounded)
