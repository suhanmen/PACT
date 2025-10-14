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
    def countOnes(n):
        """
        Helper function to count the number of 1's in the binary representation of a number.
        """
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n >>= 1
        return count
    
    return sorted(arr, key=lambda x: (countOnes(x), x))
