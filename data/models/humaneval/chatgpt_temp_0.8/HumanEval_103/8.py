def rounded_avg(n, m):
    if n > m:
        return -1
    sum = 0
    count = 0
    for i in range(n, m + 1):
        sum += i
        count += 1
    avg = round(sum / count)
    return bin(avg)
