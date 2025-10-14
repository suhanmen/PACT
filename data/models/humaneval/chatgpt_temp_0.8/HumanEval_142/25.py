def sum_squares(lst):
    total = 0
    for i, x in enumerate(lst):
        if i % 3 == 0:
            x = x ** 2
        elif i % 4 == 0:
            x = x ** 3
        total += x
    return total
