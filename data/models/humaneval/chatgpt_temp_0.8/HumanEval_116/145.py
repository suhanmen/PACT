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
    def count_ones(n):
        # This function counts the number of ones in the binary representation of n
        # We use bin(n) to convert n to binary, and then count the number of ones using str.count()
        return bin(n).count('1')

    # We first filter out negative numbers from the array
    non_negative = [x for x in arr if x >= 0]

    # We sort the non-negative numbers by their number of ones in binary representation, and then by decimal value
    sorted_non_negative = sorted(non_negative, key=lambda x: (count_ones(x), x))

    # We then create a copy of the original array with negative numbers only, and sort them in descending order
    negative = [x for x in arr if x < 0]
    sorted_negative = sorted(negative, reverse=True)

    # We concatenate the sorted negative array with the sorted non-negative array
    sorted_arr = sorted_negative + sorted_non_negative

    # We return the sorted array
    return sorted_arr
