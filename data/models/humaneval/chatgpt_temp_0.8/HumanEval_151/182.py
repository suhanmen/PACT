def double_the_difference(lst):
    sum_squares = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            sum_squares += num ** 2
    return sum_squares * 2
