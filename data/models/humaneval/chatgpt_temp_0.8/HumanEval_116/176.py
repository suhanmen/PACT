def sort_array(arr):
    def count_ones(n):
        return bin(n).count('1')
    return sorted(arr, key=lambda n: (count_ones(n), n))
