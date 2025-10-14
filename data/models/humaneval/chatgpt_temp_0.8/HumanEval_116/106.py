def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    def count_bits(num):
        """helper function to count number of ones in binary representation of a number"""
        count = 0
        while num > 0:
            count += num & 1
            num >>= 1
        return count

    # sort the array based on number of ones in binary representation and decimal value
    return sorted(arr, key=lambda x: (count_bits(x), x))
