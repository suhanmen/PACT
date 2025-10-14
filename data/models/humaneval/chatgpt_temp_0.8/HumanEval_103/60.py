def rounded_avg(n, m):
    if n > m:
        return -1
    count = m - n + 1
    total = (n + m) * count // 2
    avg = round(total / count)
    return bin(avg)
