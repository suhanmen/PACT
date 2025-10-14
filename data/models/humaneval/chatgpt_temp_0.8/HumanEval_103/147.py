def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        total = sum(range(n, m+1))
        avg = round(total / (m-n+1))
        return bin(avg)
