def sort_array(array):
    # Make a copy of the input array
    sorted_array = array.copy()

    # Determine if the sum of first and last elements is odd or even
    if len(sorted_array) > 1:
        sum_first_last = sorted_array[0] + sorted_array[-1]
        if sum_first_last % 2 == 1:
            # Sort the array in ascending order
            sorted_array.sort()
        else:
            # Sort the array in descending order
            sorted_array.sort(reverse=True)

    return sorted_array
