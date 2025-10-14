python
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.
    """
    def count_ones(n):
        """Returns the number of ones in the binary representation of n."""
        return bin(n).count('1')
    
    # Sort the array based on the number of ones in the binary representation,
    # breaking ties based on decimal value.
    return sorted(arr, key=lambda x: (count_ones(x), x))
