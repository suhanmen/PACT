def double_the_difference(lst):
    odd_numbers = [num for num in lst if isinstance(num, int) and num > 0 and num % 2 != 0]
    return sum([num ** 2 for num in odd_numbers]) * 2
