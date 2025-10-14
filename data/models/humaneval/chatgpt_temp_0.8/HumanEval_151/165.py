def double_the_difference(lst):
    sum = 0
    for num in lst:
        if num > 0 and isinstance(num, int) and num % 2 != 0:
            sum += num ** 2
    return sum * 2
