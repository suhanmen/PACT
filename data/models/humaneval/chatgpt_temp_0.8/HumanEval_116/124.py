def sort_array(arr):
    def count_ones(x):
        return bin(x).count('1')

    return sorted(arr, key=lambda x: (count_ones(x), x))
