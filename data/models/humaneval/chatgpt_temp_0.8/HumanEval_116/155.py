def sort_array(arr):
    def count_ones(val):
        return bin(val).count('1')
    
    return sorted(arr, key=lambda x: (count_ones(x), x))
