def sort_array(array):
    # Make a copy of the given array
    sorted_array = array.copy()
    # Check if the sum of the first and last element is odd or even
    if (sorted_array and (sorted_array[0] + sorted_array[-1]) % 2 == 1):
        # Sort the array in ascending order
        sorted_array.sort()
    else:
        # Sort the array in descending order
        sorted_array.sort(reverse=True)
    return sorted_array
