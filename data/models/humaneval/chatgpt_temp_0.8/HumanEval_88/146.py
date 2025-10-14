def sort_array(array):
    # Create a copy of the given array so that we don't modify the original
    sorted_array = array.copy()

    # Check if the sum of the first and last elements is odd
    if (sorted_array and (sorted_array[0] + sorted_array[-1]) % 2 == 1):
        # Sort the array in ascending order
        sorted_array.sort()
    else:
        # Sort the array in descending order
        sorted_array.sort(reverse=True)

    return sorted_array
