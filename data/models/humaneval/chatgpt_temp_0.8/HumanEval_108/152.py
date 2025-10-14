def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0
    for num in arr:
        if num == 0:
            continue
        if num < 0:
            num = str(num)[1:]
            if int(num[0]) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                num = '-' + num
        digits_sum = sum(int(digit) for digit in str(num))
        if digits_sum > 0:
            count += 1
    return count
