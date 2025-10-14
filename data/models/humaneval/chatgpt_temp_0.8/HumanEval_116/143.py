def sort_array(arr):
    def count_ones(num):
        return bin(num).count('1')

    return sorted(arr, key=lambda x: (count_ones(x), x))

assert(sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5])
assert(sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2])
assert(sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4])
