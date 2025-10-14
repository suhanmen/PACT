def double_the_difference(lst):
    result = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            result += num ** 2
    return result * 2
