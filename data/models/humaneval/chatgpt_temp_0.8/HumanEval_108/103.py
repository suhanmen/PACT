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
    def sum_digits(num):
        """
        Helper function to calculate the sum of digits of a number.
        """
        if num == 0:
            return 0
        elif num > 0:
            return num % 10 + sum_digits(num // 10)
        else:
            return -1 * (abs(num) % 10 + sum_digits(abs(num) // 10))

    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1
    return count
