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
    def get_sum_of_digits(num):
        if num == 0:
            return 0
        sign = -1 if num < 0 else 1
        num = abs(num)
        sum_of_digits = 0
        while num > 0:
            sum_of_digits += sign * (num % 10)
            num //= 10
        return sum_of_digits

    count = 0
    for num in arr:
        if get_sum_of_digits(num) != 0:
            count += 1
    return count
