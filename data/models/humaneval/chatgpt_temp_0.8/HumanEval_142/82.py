def sum_squares(lst):
    total = 0  # initialize the sum to 0
    for i in range(len(lst)):
        if i % 3 == 0:  # if the index is a multiple of 3, square the entry
            total += lst[i]**2
        elif i % 4 == 0:  # if the index is a multiple of 4 but not 3, cube the entry
            total += lst[i]**3
        else:  # otherwise, add the entry as is
            total += lst[i]
    return total
