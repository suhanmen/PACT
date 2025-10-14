python
def sum_squares(lst):
    total_sum = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total_sum += num ** 2
        elif i % 4 == 0:
            total_sum += num ** 3
        else:
            total_sum += num
    return total_sum
