def sum_squares(lst):
    sum = 0
    for index, item in enumerate(lst):
        if index % 3 == 0:
            sum += item ** 2
        elif index % 4 == 0 and index % 3 != 0:
            sum += item ** 3
        else:
            sum += item
    return sum
