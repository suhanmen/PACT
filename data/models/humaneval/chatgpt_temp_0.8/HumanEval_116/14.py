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
    
    def count_ones(num):
        """
        This helper function counts the number of ones in the binary 
        representation of a non-negative integer.
        """
        binary = bin(num)[2:]
        return binary.count('1')
    
    sorted_arr = sorted(arr, key=lambda x: (count_ones(x), x))
    return sorted_arr
