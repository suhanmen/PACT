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
    def signed_digits(n):
        """
        Helper function to get the signed digits of a number
        """
        if n == 0:
            return []
        elif n > 0:
            return [int(d) for d in str(n)]
        else:
            return [-int(d) for d in str(-n)]

    count = 0
    for n in arr:
        if sum(signed_digits(n)) > 0:
            count += 1

    return count
