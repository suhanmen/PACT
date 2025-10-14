def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        avg = round(sum(range(n, m+1)) / (m - n + 1))
        return bin(avg)[0:2] + bin(avg)[2:].zfill(8)
