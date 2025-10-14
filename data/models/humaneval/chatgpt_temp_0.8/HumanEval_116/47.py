def sort_array(arr):
    def count_ones(n):
        """
        This helper function takes an integer n
        and returns the count of ones in its binary representation.
        """
        return bin(n).count('1')
    
    return sorted(arr, key=lambda x: (count_ones(x), x))
