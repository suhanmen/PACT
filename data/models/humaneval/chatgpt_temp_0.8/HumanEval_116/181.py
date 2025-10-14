def sort_array(arr):
    def count_ones(num):
        return bin(num).count('1')
    
    arr.sort(key=lambda x: (count_ones(x), x))
    return arr
