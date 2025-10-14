def move_one_ball(arr):
    if len(arr) == 0:
        # If the array is empty, it is already sorted
        return True
    
    # Find the index of the smallest element in the array
    min_index = arr.index(min(arr))
    
    # If the smallest element is already at the beginning of the array, it is already sorted
    if min_index == 0:
        return True
    
    # Otherwise, check if the array can be sorted by doing one right shift operation
    shifted_arr = arr[-1:] + arr[:-1]  # Shift all elements to the right
    sorted_shifted_arr = sorted(shifted_arr)  # Sort the shifted array
    return shifted_arr == sorted_shifted_arr  # Check if the shifted array is sorted
