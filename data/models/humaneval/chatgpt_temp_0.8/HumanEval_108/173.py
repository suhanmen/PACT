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
    def sum_digits(n):
        if n == 0:
            return 0
        elif n < 0:
            digits = [-int(d) for d in str(-n)]
        else:
            digits = [int(d) for d in str(n)]
        return sum(digits)

    return sum(1 for x in arr if sum_digits(x) > 0)
