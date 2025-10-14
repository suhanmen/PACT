def sort_array(arr):
    def count_ones(n):
        """
        Returns the number of ones in the binary representation of n.
        """
        return bin(n).count('1')

    sorted_arr = sorted(arr, key=lambda n: (count_ones(n), n))
    return sorted_arr
