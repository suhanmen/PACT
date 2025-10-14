def double_the_difference(lst):
    sum_of_odd_squares = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            sum_of_odd_squares += num ** 2
    return sum_of_odd_squares * 2
