def sum_squares(lst):
    sum = 0
    for num in lst:
        rounded_num = int(num + 0.5)
        sum += rounded_num**2
    return sum
