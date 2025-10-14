def rounded_avg(n, m):
    if n > m:
        return -1
    sum_of_integers = sum(range(n, m + 1))
    average = round(sum_of_integers / (m - n + 1))
    return bin(average)
