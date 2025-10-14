def rounded_avg(n, m):
    if n > m:
        return -1
    sum = 0
    count = m - n + 1
    for i in range(n, m+1):
        sum += i
    avg = round(sum/count)
    return bin(avg)[2:]
