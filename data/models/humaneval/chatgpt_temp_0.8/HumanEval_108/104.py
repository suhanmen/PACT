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
    def get_digit_sum(n):
        """Helper function to get the sum of digits in a number"""
        if n == 0:
            return 0
        if n < 0:
            n = -n
            sign = -1
        else:
            sign = 1
        digit_sum = 0
        while n > 0:
            digit_sum += sign * (n % 10)
            n //= 10
        return digit_sum

    count = 0
    for num in arr:
        if get_digit_sum(num) != 0:
            count += 1
    return count
