def sort_array(array):
    sorted_array = array.copy()
    is_odd_sum = (array[0] + array[-1]) % 2 == 1
    if is_odd_sum:
        sorted_array.sort()
    else:
        sorted_array.sort(reverse=True)
    return sorted_array
