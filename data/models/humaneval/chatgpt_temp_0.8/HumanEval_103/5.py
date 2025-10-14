def rounded_avg(n, m):
    if n > m:
        return -1
    average = round((n + m) / 2)
    return bin(average)[2:]
