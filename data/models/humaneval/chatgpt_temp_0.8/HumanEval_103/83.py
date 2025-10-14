def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round(sum(range(n, m+1)) / (m - n + 1)) # calculate the average and round it
    return bin(avg)[2:] # convert the rounded average to binary and return it as a string
