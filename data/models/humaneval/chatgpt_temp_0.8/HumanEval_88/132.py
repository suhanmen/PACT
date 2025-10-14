def sort_array(array):
    # Make a copy of the input array
    sorted_array = array.copy()

    # Determine whether to sort in ascending or descending order
    if (sorted_array and (sorted_array[0] + sorted_array[-1]) % 2 == 1):
        sorted_array.sort()
    else:
        sorted_array.sort(reverse=True)

    return sorted_array
