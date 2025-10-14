def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        avg = int(round(sum(range(n, m+1)) / float(m-n+1)))
        return bin(avg)
