def sort_array(arr):
    def count_ones(n):
        """
        Helper function to count the number of ones in the binary representation of a number
        """
        return bin(n).count('1')

    return sorted(arr, key=lambda x: (count_ones(x), x))
