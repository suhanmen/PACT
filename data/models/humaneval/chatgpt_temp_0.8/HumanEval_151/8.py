def double_the_difference(lst):
    result = 0
    for num in lst:
        if num > 0 and num % 2 != 0 and isinstance(num, int):
            result += num ** 2
    return 2 * result
