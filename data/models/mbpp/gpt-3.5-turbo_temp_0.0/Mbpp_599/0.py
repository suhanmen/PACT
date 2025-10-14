def sum_average(n):
    sum_of_numbers = sum(range(1, n+1))
    average = sum_of_numbers / n
    return sum_of_numbers, average

assert sum_average(10) == (55, 5.5)