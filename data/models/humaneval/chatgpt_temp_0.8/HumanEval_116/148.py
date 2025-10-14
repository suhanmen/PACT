def sort_array(arr):
    sorted_arr = sorted(arr, key=lambda x: (bin(x).count("1"), x))
    return sorted_arr
