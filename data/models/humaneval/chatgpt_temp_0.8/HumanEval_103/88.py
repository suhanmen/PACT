def rounded_avg(n, m):
    if n > m:
        return -1
    avg = sum(range(n, m+1)) / (m - n + 1)
    return bin(round(avg))[0:2] + bin(round(avg))[2:]
