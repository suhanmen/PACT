def sort_array(array):
    # Make a copy of the given array
    sorted_array = array[:]
    
    # Check if the sum of the first and last elements is odd or even
    if (sorted_array and sorted_array[0] + sorted_array[-1]) % 2 == 1:
        # Sort the array in ascending order
        sorted_array.sort()
    else:
        # Sort the array in descending order
        sorted_array.sort(reverse=True)
    
    # Return the sorted array
    return sorted_array
