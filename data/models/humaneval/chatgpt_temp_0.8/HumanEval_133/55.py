def sum_squares(lst):
    total = 0
    for num in lst:
        total += int(num + 0.5) ** 2
    return total
