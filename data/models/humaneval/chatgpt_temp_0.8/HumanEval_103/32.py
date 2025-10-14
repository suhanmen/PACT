def rounded_avg(n, m):
    if n > m:
        return -1
    average = round(sum(range(n, m+1))/float(m-n+1))
    return bin(average)
