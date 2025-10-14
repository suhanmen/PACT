def sum_squares(lst):
    square_sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            square_sum += lst[i] ** 2
        elif i % 4 == 0:
            square_sum += lst[i] ** 3
        else:
            square_sum += lst[i]
    return square_sum
