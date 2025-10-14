def rounded_avg(n, m):
    if n > m:
        return -1
    total = 0
    count = 0
    for i in range(n, m+1):
        total += i
        count += 1
    avg = round(total / count)
    return bin(avg)
