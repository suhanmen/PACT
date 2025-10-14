def double_the_difference(lst):
    square_sum = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 == 1:
            square_sum += num ** 2
    return square_sum * 2
