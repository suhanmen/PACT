def sum_squares(lst):
    total = 0
    for num in lst:
        num = int(num + 0.5)
        total += num*num
    return total
