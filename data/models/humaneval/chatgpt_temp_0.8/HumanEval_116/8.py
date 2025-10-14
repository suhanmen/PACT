def sort_array(arr):
    arr.sort(reverse=True)
    return sorted(arr, key=lambda x: bin(x).count("1"))
